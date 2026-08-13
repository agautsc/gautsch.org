#!/usr/bin/env python
"""Turn a LinkedIn data export into content/notes/ pages.

Usage (from the repo root):
    python scripts/import_linkedin.py --export <dir with Shares_*.csv> [--write]

Runs read-only by default and prints what it would do. Pass --write to touch disk.

Three things here are not obvious and are the reason this is a script and not a
one-off paste:

1. LinkedIn wraps every *line* of a post in a double quote before writing the CSV
   field, and the field's opening wrapper quote doubles as the CSV field-opening
   quote. So after csv parsing, line 1 has a stray trailing quote and lines 2+ are
   wrapped on both sides. Unwrapping has to be positional. See unwrap().
2. Posts already republished by hand into content/archive/ must not be imported
   again -- they are live URLs with aliases pointing at them.
3. The 08-08 media download saved every URL as .jpg regardless of what came back.
   Roughly one in six is actually an MP4. Extensions are corrected from magic bytes.
"""

import argparse
import collections
import csv
import difflib
import glob
import os
import re
import shutil
import sys
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES = os.path.join(REPO, "content", "notes")
ARCHIVE = os.path.join(REPO, "content", "archive")
MEDIA = os.path.join(REPO, "static", "linkedin-media")
VIDEO_HOLD = os.path.join(REPO, "_linkedin-video")  # untracked; source for YouTube uploads

IMAGE_EXT = {"JPEG": ".jpg", "PNG": ".png", "GIF": ".gif"}


# --------------------------------------------------------------------------- time

def eastern(dt_utc):
    """US Eastern for a UTC datetime, using the 2007+ rule.

    zoneinfo has no tz database on the Windows boxes this runs on, and the whole
    corpus (2012-2026) postdates the 2007 DST change, so the rule is safe to inline.
    DST: second Sunday in March 02:00 local -> first Sunday in November 02:00 local.
    """
    y = dt_utc.year
    march = datetime(y, 3, 8, tzinfo=timezone.utc)
    start = march + timedelta(days=(6 - march.weekday()) % 7, hours=7)  # 2am EST = 07:00Z
    nov = datetime(y, 11, 1, tzinfo=timezone.utc)
    end = nov + timedelta(days=(6 - nov.weekday()) % 7, hours=6)  # 2am EDT = 06:00Z
    offset = -4 if start <= dt_utc < end else -5
    return dt_utc.astimezone(timezone(timedelta(hours=offset)))


# ---------------------------------------------------------------------- text prep

def unwrap(field):
    """Undo LinkedIn's per-line quote wrapping. See module docstring, point 1."""
    if not field:
        return ""
    lines = field.split("\n")
    out = []
    for i, line in enumerate(lines):
        line = line.rstrip("\r")
        if line == '""':
            out.append("")
            continue
        # Line 1's opening wrapper was consumed by the CSV reader as the field quote.
        if i > 0 and line.startswith('"'):
            line = line[1:]
        if line.endswith('"'):
            line = line[:-1]
        out.append(line)
    text = "\n".join(out)
    return text.replace("\xa0", " ").replace("​", "").strip()


def paragraphs(text):
    """Collapse runs of blank lines; return a list of paragraph strings."""
    paras, buf = [], []
    for line in text.split("\n"):
        if line.strip():
            buf.append(line.strip())
        elif buf:
            paras.append(" ".join(buf))
            buf = []
    if buf:
        paras.append(" ".join(buf))
    return paras


def escape_markdown(para):
    """Neutralise only the constructs that change meaning at line start.

    Hashtags are the common case: '#AI' opening a line would render as an <h1>.
    """
    return re.sub(r"^(#{1,6}\s|[-*+]\s|>\s|\d+\.\s)", lambda m: "\\" + m.group(1), para)


SENTENCE_END = re.compile(r"(?<=[.!?])\s")


def derive_title(text, limit=72):
    """First sentence, trimmed to a word boundary. Posts have no titles of their own.

    Link posts often open with a bare URL on its own line; stripping URLs would leave
    that paragraph empty, so walk on to the first paragraph that has words in it.
    """
    first = ""
    for para in paragraphs(text):
        candidate = re.sub(r"https?://\S+", "", para).strip()
        if re.search(r"[A-Za-z0-9]", candidate):
            first = candidate
            break
    if not first:
        return "Untitled note"
    first = re.sub(r"\s+", " ", first)
    parts = SENTENCE_END.split(first, 1)
    title = parts[0].strip() if parts else first
    if len(title) > limit:
        cut = title[:limit].rsplit(" ", 1)[0]
        title = cut.rstrip(",;:-— ") + "…"
    title = title.strip().strip('"').strip()
    return title or "Untitled note"


def slugify(title, taken):
    s = title.lower()
    s = s.replace("&", " and ")
    s = re.sub(r"[‘’']", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    s = "-".join(s.split("-")[:9])[:60].strip("-") or "note"
    base, n = s, 2
    while s in taken:
        s = f"{base}-{n}"
        n += 1
    taken.add(s)
    return s


def summarise(text, limit=155):
    flat = re.sub(r"\s+", " ", " ".join(paragraphs(text))).strip()
    if len(flat) <= limit:
        return flat
    return flat[:limit].rsplit(" ", 1)[0].rstrip(",;:-— ") + "…"


def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


# -------------------------------------------------------------------------- media

def sniff(path):
    with open(path, "rb") as fh:
        head = fh.read(16)
    if head[:3] == b"\xff\xd8\xff":
        return "JPEG"
    if head[:8] == b"\x89PNG\r\n\x1a\n":
        return "PNG"
    if head[4:8] == b"ftyp":
        return "MP4"
    if head[:4] == b"GIF8":
        return "GIF"
    return "OTHER"


MEDIA_DATE = re.compile(r"on ([A-Z][a-z]+ \d{1,2}, \d{4}) at (\d{1,2}:\d{2} [AP]M)")


ORPHAN_HOLD = os.path.join(REPO, "_linkedin-orphans")  # untracked; media with no post


def media_index(write):
    """Map 'YYYY-MM-DD HH:MM' (UTC) -> media files, correcting extensions as we go.

    Videos and HLS sidecars are moved out of static/ into VIDEO_HOLD: they are the
    YouTube upload queue, not something to commit into a Pages repo.
    """
    # The downloader drops manifest.csv into static/, where Hugo would publish it
    # (it holds signed licdn URLs). It gets moved next to this script; accept either.
    manifest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "linkedin-media-manifest.csv")
    if not os.path.exists(manifest):
        manifest = os.path.join(MEDIA, "manifest.csv")
    if not os.path.exists(manifest):
        sys.exit("no media manifest found -- run the media download first")

    # A previous run renames files and moves some of them out of static/, so a row's
    # File value ("2021-01-19-093.jpg") may now be a .png here or an .mp4 next door.
    # Resolve by stem across all three folders to keep re-runs idempotent.
    located = {}
    for folder in (MEDIA, VIDEO_HOLD, ORPHAN_HOLD):
        if os.path.isdir(folder):
            for f in os.listdir(folder):
                if not f.endswith(".csv"):
                    located.setdefault(os.path.splitext(f)[0], os.path.join(folder, f))

    index, videos = {}, {}
    with open(manifest, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            src = located.get(os.path.splitext(row["File"])[0])
            if not src:
                continue
            m = MEDIA_DATE.search(row["SourceDateTime"])
            if not m:
                continue
            stamp = datetime.strptime(f"{m.group(1)} {m.group(2)}", "%B %d, %Y %I:%M %p")
            key = stamp.strftime("%Y-%m-%d %H:%M")

            kind = sniff(src)
            stem = os.path.splitext(row["File"])[0]
            if kind in IMAGE_EXT:
                # Pull images back into static/ even if a prior run parked them in
                # _linkedin-orphans/ -- the date fallback may have found them a post.
                name = stem + IMAGE_EXT[kind]
                dest = os.path.join(MEDIA, name)
                if write and os.path.abspath(dest) != os.path.abspath(src):
                    os.replace(src, dest)
                index.setdefault(key, []).append(name)
            else:
                name = stem + (".mp4" if kind == "MP4" else ".bin")
                dest = os.path.join(VIDEO_HOLD, name)
                if write and os.path.abspath(dest) != os.path.abspath(src):
                    os.makedirs(VIDEO_HOLD, exist_ok=True)
                    os.replace(src, dest)
                if kind == "MP4":
                    videos.setdefault(key, []).append(name)
    return index, videos


# ------------------------------------------------------------------ archive dedupe

def norm(s):
    s = re.sub(r"\{\{.*?\}\}", "", s or "")
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    return " ".join(s.split())


def archive_fingerprints():
    """Text of every post already republished by hand, so we never import it twice."""
    prints = []
    for path in sorted(glob.glob(os.path.join(ARCHIVE, "*.md"))):
        if os.path.basename(path) == "_index.md":
            continue
        raw = open(path, encoding="utf-8").read()
        title, body = "", raw
        if raw.startswith("---"):
            fm, _, body = raw[3:].partition("\n---")
            tm = re.search(r'^title:\s*"?(.*?)"?\s*$', fm, re.M)
            title = tm.group(1) if tm else ""
        prints.append((os.path.basename(path), norm(title), norm(body)))
    return prints


def already_published(text, prints, threshold=0.60):
    """Match on body, and fall back to title.

    The title fallback exists for one-liner posts that were republished with the
    post text *as* the title and an empty body -- the pen post is the example.
    """
    n = norm(text)
    if not n:
        return None
    for name, ntitle, nbody in prints:
        if nbody.strip():
            if difflib.SequenceMatcher(None, n[:600], nbody[:600]).ratio() >= threshold:
                return name
        if ntitle and difflib.SequenceMatcher(None, n[:120], ntitle[:120]).ratio() >= 0.75:
            return name
    return None


# --------------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--export", required=True, help="directory holding Shares_*.csv")
    ap.add_argument("--write", action="store_true", help="actually write files")
    args = ap.parse_args()

    shares = glob.glob(os.path.join(args.export, "Shares_*.csv"))
    if not shares:
        sys.exit(f"no Shares_*.csv in {args.export}")

    with open(shares[0], encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    images, videos = media_index(args.write)
    prints = archive_fingerprints()

    # Rich_Media stamps the *upload* minute and Shares stamps the *publish* minute,
    # so a slow upload leaves photos stranded a few minutes off their post. Fall the
    # match back to the day — but only when that day holds exactly one post and one
    # unmatched media group, which is the only case where the pairing is unambiguous.
    minutes_by_day = collections.defaultdict(list)
    for key in images:
        minutes_by_day[key[:10]].append(key)
    posts_by_day = collections.Counter(r["Date"][:10] for r in rows)
    exact = {r["Date"][:16] for r in rows}
    for day, keys in minutes_by_day.items():
        stranded = [k for k in keys if k not in exact]
        if posts_by_day.get(day) == 1 and len(stranded) == 1 and len(keys) == 1:
            same_day = next(r["Date"][:16] for r in rows if r["Date"].startswith(day))
            images.setdefault(same_day, []).extend(images.pop(stranded[0]))

    if args.write:
        os.makedirs(NOTES, exist_ok=True)

    taken, written = set(), 0
    skipped_empty, skipped_dupe, video_queue = [], [], []
    used_media = set()

    for row in rows:
        text = unwrap(row.get("ShareCommentary"))
        stamp = row["Date"].strip()
        if not text:
            skipped_empty.append(stamp)
            continue
        dupe = already_published(text, prints)
        if dupe:
            skipped_dupe.append((stamp, dupe))
            continue

        utc = datetime.strptime(stamp, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
        local = eastern(utc)
        key = utc.strftime("%Y-%m-%d %H:%M")

        title = derive_title(text)
        slug = slugify(title, taken)
        body = "\n\n".join(escape_markdown(p) for p in paragraphs(text))

        fm = [
            "---",
            f"title: {yaml_str(title)}",
            f"date: {local.isoformat()}",
            f"slug: {yaml_str(slug)}",
            f"summary: {yaml_str(summarise(text))}",
        ]
        link = (row.get("ShareLink") or "").strip()
        if link:
            fm.append(f"linkedin: {yaml_str(link)}")
        shared = (row.get("SharedUrl") or "").strip()
        if shared:
            fm.append(f"sharedurl: {yaml_str(shared)}")
        if key in images:
            fm.append("photos:")
            fm += [f"  - {yaml_str('/linkedin-media/' + n)}" for n in sorted(images[key])]
            used_media.update(images[key])
        if key in videos:
            # Placeholder: fill in the id after the upload, and the embed replaces
            # the "watch on LinkedIn" fallback automatically.
            fm.append('youtube: ""')
            video_queue.append((stamp, slug, title, videos[key]))
        fm += ["draft: false", "---", ""]

        out = os.path.join(NOTES, f"{local.strftime('%Y-%m-%d')}-{slug}.md")
        if args.write:
            with open(out, "w", encoding="utf-8", newline="\n") as fh:
                fh.write("\n".join(fm) + body + "\n")
        written += 1

    # Anything left in static/ that no note points at would be published at a
    # guessable URL with no context around it. Those belong in the local backup.
    orphans = sorted(
        f for f in os.listdir(MEDIA)
        if os.path.splitext(f)[1].lower() in {".jpg", ".png", ".gif"} and f not in used_media
    )
    if args.write and orphans:
        os.makedirs(ORPHAN_HOLD, exist_ok=True)
        for f in orphans:
            os.replace(os.path.join(MEDIA, f), os.path.join(ORPHAN_HOLD, f))

    print(f"notes written : {written}")
    print(f"skipped empty : {len(skipped_empty)}")
    print(f"skipped dupes : {len(skipped_dupe)} (already in content/archive/)")
    for stamp, name in skipped_dupe:
        print(f"    {stamp}  <- {name}")
    print(f"photos attached   : {len(used_media)}")
    print(f"orphaned media    : {len(orphans)} (no matching post; moved to _linkedin-orphans/)")
    print(f"\nvideo posts needing a YouTube upload: {len(video_queue)}")
    for stamp, slug, title, files in video_queue:
        print(f"    {stamp}  {slug}\n        {title}\n        {', '.join(files)}")
    if not args.write:
        print("\n(dry run -- nothing written; pass --write)")


if __name__ == "__main__":
    main()
