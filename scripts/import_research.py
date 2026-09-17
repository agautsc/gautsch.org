#!/usr/bin/env python3
"""Import the Acemoglu rabbit-hole material from the Obsidian vault into content/research/.

Source of truth is the vault, not this repo: the annotated transcript carries the
anchors, and the eighteen pages carry their own short versions. Re-run this after
any content pass in the vault and the site follows. Nothing is fetched at build
time -- the transcript is written into the repo here, once.

Usage:  python3 scripts/import_research.py [--vault DIR] [--write]
"""
import argparse, html, io, json, os, re, sys, unicodedata

TRANSCRIPT = "Daron Acemoglu on Liberalism, Automation, and the Educated Elite (Ep. 286).md"
PAGES_DIR  = "Rabbit Holes"
INDEX_PAGE = "Acemoglu Ep 286 - Rabbit Hole Index"
EPISODE_URL = "https://conversationswithtyler.com/episodes/daron-acemoglu-2/"
AUDIO_URL   = "https://traffic.libsyn.com/secure/cowenconvos/CWT-292-DaronAcemoglu-Podcast-v2.mp3?dest-id=850607"

def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    return re.sub(r"[-\s]+", "-", s)

def read(p):
    with io.open(p, encoding="utf-8") as source:
        return source.read().replace("\xa0", " ")

# ---------- markdown -> html for transcript prose ----------
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" rel="nofollow">\1</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t, flags=re.S)
    t = re.sub(r"(?<!\w)_(.+?)_(?!\w)", r"<em>\1</em>", t, flags=re.S)
    # bold is already <strong> above, so a surviving single * is emphasis.
    # Without this the popovers rendered literal asterisks (found 2026-09-08).
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", t, flags=re.S)
    return t

def load_pages(vault):
    pages = {}
    d = os.path.join(vault, PAGES_DIR)
    for f in sorted(os.listdir(d)):
        if not f.endswith(".md") or f[:-3] == INDEX_PAGE:
            continue
        title = f[:-3]
        s = read(os.path.join(d, f))
        fm = re.match(r"^---\n(.*?)\n---\n", s, re.S)
        meta, body = (fm.group(1), s[fm.end():]) if fm else ("", s)
        def field(k):
            m = re.search(rf"^{k}:\s*(.+)$", meta, re.M)
            return m.group(1).strip().strip('"') if m else None
        short = re.search(r"^> \*\*The short version\*\*\s*[—-]\s*(.+)$", body, re.M)
        asked = re.search(r"^\*\*Adam asked:\*\*\s*\*?[\"“](.+?)[\"”]\*?\s*$", body, re.M)
        tl = field("transcript_line")
        pages[title] = {
            "title": title,
            "slug": slugify(title),
            "transcript_line": int(tl) if tl and tl.isdigit() else None,
            "short": short.group(1).strip() if short else None,
            "asked": asked.group(1).strip() if asked else None,
            "body": body,
        }
    return pages

def parse_transcript(vault, pages):
    raw = read(os.path.join(vault, TRANSCRIPT))
    start = raw.find("**TYLER COWEN:** Hello, everyone")
    if start < 0:
        sys.exit("could not find the transcript opening line")
    for stop in ("\n---\n\n# Review Session", "\n# Review Session"):
        k = raw.find(stop, start)
        if k > 0:
            raw = raw[:k]
    body = raw[start:]

    # line number -> paragraph index, so frontmatter transcript_line values resolve
    paras, line_of = [], {}
    cur = raw.index(body)
    for chunk in body.split("\n\n"):
        p = chunk.strip()
        if not p:
            continue
        off = raw.index(p, cur); cur = off + len(p)
        line_of[len(paras)] = raw[:off].count("\n") + 1
        paras.append(p)

    by_title = {t: p for t, p in pages.items()}
    anchors = []          # one per (page, position) pair
    rendered = []

    for i, p in enumerate(paras):
        links = re.findall(r"\*\*→ \[\[(.+?)\]\]\*\*", p)
        # strip Adam's private margin notes: the italic prompt plus its arrow link
        clean = re.sub(r"\s*\*[^*\n]+\*\s*\*\*→ \[\[.+?\]\]\*\*", "", p)
        clean = re.sub(r"\s*\*\*→ \[\[.+?\]\]\*\*", "", clean)
        rendered.append({"i": i, "line": line_of[i], "md": clean, "links": links})
        for t in links:
            if t in by_title:
                anchors.append({"page": t, "para": i, "via": "link"})

    # pages with no arrow link in the transcript fall back to their transcript_line
    linked = {a["page"] for a in anchors}
    para_of_line = sorted(line_of.items(), key=lambda kv: kv[1])
    for t, pg in pages.items():
        if t in linked or not pg["transcript_line"]:
            continue
        best = min(para_of_line, key=lambda kv: abs(kv[1] - pg["transcript_line"]))
        anchors.append({"page": t, "para": best[0], "via": "transcript_line"})

    # render paragraphs, wrapping highlights and attaching anchors
    by_para = {}
    for a in anchors:
        by_para.setdefault(a["para"], []).append(a)

    out, n = [], 0
    for r in rendered:
        md, i = r["md"], r["i"]
        mine = by_para.get(i, [])
        # an explicit arrow link beats a transcript_line fallback for the visible link
        mine.sort(key=lambda m: 0 if m["via"] == "link" else 1)
        target = pages[mine[0]["page"]] if mine else None
        aid = None
        if target:
            n += 1
            aid = f"a{n:02d}"
            for m in mine:                    # every page anchored here shares the id
                pages[m["page"]].setdefault("anchor", aid)
        used = []                      # a paragraph can hold two highlights; the id
        def wrap(m):                   # belongs to the first, or it is duplicated
            inner = inline(m.group(1))
            if not target:
                return f'<mark class="rh-hl">{inner}</mark>'
            idattr = "" if used else f' id="{aid}"'
            used.append(1)
            href = f'/research/{target["slug"]}/'
            link = (f'<a class="rh-mark"{idattr} href="{href}"'
                    f' aria-describedby="pop-{target["slug"]}">{inner}</a>')
            short = inline(target["short"]) if target.get("short") else ""
            pop = (f'<span class="rh-pop" id="pop-{target["slug"]}" role="tooltip">'
                   f'<span class="rh-pop-title">{html.escape(target["title"])}</span>'
                   f'<span class="rh-pop-short">{short}</span>'
                   f'<a class="rh-pop-more" href="{href}">Read more &rarr;</a>'
                   f'</span>')
            return f'<span class="rh-anno">{link}{pop}</span>'
        out.append({"i": i, "line": r["line"], "html": render_para(md, wrap, aid),
                    "anchor": aid, "pages": [m["page"] for m in mine],
                    "highlighted": "==" in md})
    return out, anchors, paras

def render_para(md, wrap, aid=None):
    """Escape + inline-format, then wrap highlight spans, without double-escaping.

    A paragraph anchored by transcript_line rather than by an arrow link has no
    ==highlight== to carry the id, so the id goes on the paragraph itself --
    otherwise the page's back-link would point at an element that is not there.
    """
    parts, last = [], 0
    for m in re.finditer(r"==(.+?)==", md, re.S):
        parts.append(("text", md[last:m.start()]))
        parts.append(("hl", m.group(1)))
        last = m.end()
    parts.append(("text", md[last:]))
    buf = []
    for kind, t in parts:
        if kind == "text":
            buf.append(inline(t))
        else:
            buf.append(wrap(re.match(r"(.*)", t, re.S)))
    s = "".join(buf)
    # the transcript carries "## On automation"-style section headings that match
    # the episode's own chapter markers; they are headings, not prose
    h = re.match(r"##\s+(.+?)\s*$", md.strip(), re.S)
    if h:
        anchor = f' id="{aid}"' if aid else ""
        return f'<h2 class="rh-chapter"{anchor}>{inline(h.group(1))}</h2>'
    carries_id = aid and 'id="' not in s
    idattr = f' id="{aid}"' if carries_id else ""
    m = re.match(r"<strong>([A-Z][A-Z\s.]+:)</strong>\s*(.*)$", s, re.S)
    if m:
        return (f'<p class="rh-turn"{idattr}><strong class="rh-speaker">{m.group(1)}</strong> '
                f'{m.group(2)}</p>')
    return f"<p{idattr}>{s}</p>"

def clean_asked(text):
    """Render a two-part question readably in the `asked:` front matter.

    A body line like  **Adam asked:** *"First?"* and *"Second?"*  captures as
    First?"* and *"Second?  -- the emphasis markers and the inner straight quotes
    both survive. Drop the markers and turn the inner quotes into curly ones,
    alternating closing/opening because the capture starts inside a quotation.
    """
    out, inside = [], True
    for ch in text.replace("*", ""):
        if ch == '"':
            out.append("\u201d" if inside else "\u201c")
            inside = not inside
        else:
            out.append(ch)
    return "".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default="/home/agautsc/Documents/ARG Full")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()

    pages = load_pages(a.vault)
    paras, anchors, _ = parse_transcript(a.vault, pages)

    anchored = {p["title"] for p in pages.values() if p.get("anchor")}
    print(f"pages: {len(pages)}   anchored: {len(anchored)}   unanchored: {len(pages)-len(anchored)}")
    for t, p in sorted(pages.items()):
        if not p.get("anchor"):
            print("   ! no anchor:", t)
    print(f"paragraphs: {len(paras)}   with highlight: {sum(1 for p in paras if p['highlighted'])}")
    print(f"short versions: {sum(1 for p in pages.values() if p['short'])}/{len(pages)}")

    figures = load_site_figures()
    rendered_pages = {
        t: resolve_wikilinks(render_site_figures(strip_page_frontmatter_artifacts(p["body"]), p["slug"], figures), pages, t)
        for t, p in pages.items()
    }

    root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content", "research")
    for t, p in pages.items():
        existing = os.path.join(root, p["slug"], "index.md")
        if os.path.exists(existing):
            validate_review_provenance(read(existing), rendered_pages[t], p["slug"])

    if not a.write:
        print("\n[dry-run] nothing written. pass --write")
        return

    os.makedirs(root, exist_ok=True)

    tbody = "\n".join(p["html"] for p in paras)
    idx = io.open(os.path.join(root, "_index.md"), "w", encoding="utf-8")
    idx.write("---\n")
    idx.write('title: "An Economic Robotic Rabbit Hole"\n')
    # Search/share description only; the page no longer shows it (Adam, 2026-09-17).
    idx.write('description: "Tyler Cowen and Daron Acemoglu, annotated. The highlighted passages open the places I stopped to learn more."\n')
    idx.write("layout: transcript\n")
    idx.write(f'source_url: "{EPISODE_URL}"\n')
    # Mercatus's own file, from the show's published feed at
    # https://cowenconvos.libsyn.com/rss (found 2026-09-08). Nothing is rehosted.
    # 49,358,097 bytes, Accept-Ranges: bytes, CORS *, so seeking and follow-along work.
    idx.write(f'audio_url: "{AUDIO_URL}"\n')
    idx.write("draft: false\n")
    idx.write("---\n\n")
    idx.write('<div class="rh-transcript">\n' + tbody + "\n</div>\n")
    idx.close()

    descriptions = load_descriptions()
    for t, p in pages.items():
        d = os.path.join(root, p["slug"]); os.makedirs(d, exist_ok=True)
        f = io.open(os.path.join(d, "index.md"), "w", encoding="utf-8")
        f.write("---\n")
        f.write(f'title: "{t}"\n')
        if p["slug"] not in descriptions:
            raise ValueError(f"{p['slug']}: add a description to data/research/descriptions.yaml")
        f.write(f'description: {json.dumps(descriptions[p["slug"]], ensure_ascii=False)}\n')
        if p["short"]:
            f.write("short_version: |\n  " + p["short"].replace("\n", "\n  ") + "\n")
        if p["asked"]:
            f.write(f'asked: "{clean_asked(p["asked"])}"\n')
        if p.get("anchor"):
            f.write(f'transcript_anchor: "{p["anchor"]}"\n')
        models = ['Claude', 'Codex'] if p['slug'] in figures else ['Claude']
        f.write('models: ' + json.dumps(models) + '\n')
        f.write("draft: false\n---\n\n")
        f.write(rendered_pages[t])
        f.close()
    print(f"\nwrote content/research/_index.md and {len(pages)} pages")

def validate_review_provenance(existing, incoming, slug):
    """Do not silently undo the book review with an older vault copy.

    This checks known provenance markers, not factual accuracy or every edit.
    Reconcile source copies before intentionally removing reviewed material.
    """
    markers = (r"^## From the book\s*$", r"checked against the audiobook edition", r"<!-- reader-review: 2026-09-15 -->")
    for marker in markers:
        if re.search(marker, existing, re.I | re.M) and not re.search(marker, incoming, re.I | re.M):
            raise ValueError(f"{slug}: import would remove book-review material; reconcile the vault source with the site before importing")


def load_descriptions():
    """Search/share descriptions, one per slug, from data/research/descriptions.yaml.

    Flat `slug: "text"` lines only, so no YAML dependency is needed."""
    path = os.path.join(os.path.dirname(__file__), "..", "data", "research", "descriptions.yaml")
    out = {}
    with open(path, encoding="utf-8") as source:
        for line in source:
            m = re.match(r'^([a-z0-9-]+):\s*"(.*)"\s*$', line)
            if m:
                out[m.group(1)] = m.group(2).replace('\\"', '"')
    return out

def load_site_figures():
    """Map source pages to curated figures and their preserved Mermaid input."""
    directory = os.path.join(os.path.dirname(__file__), "..", "data", "research")
    with open(os.path.join(directory, "figures.json"), encoding="utf-8") as source:
        figures = {
            value["slug"]: {"source": value["source_mermaid"],
                            "shortcode": '{{< research-figure "' + key + '" >}}'}
            for key, value in json.load(source).items()
        }
    with open(os.path.join(directory, "printing.json"), encoding="utf-8") as source:
        figures["the-printing-press-how-long-was-the-adjustment"] = {
            "source": json.load(source)["source_mermaid"],
            "shortcode": '{{< printing-timeline >}}',
        }
    return figures


def render_site_figures(body, slug, figures=None):
    """Preserve vault diagrams; render readable figures at the content boundary.

    Reconcile changed source diagrams with data/research before replacing them.
    This runs for every page before any output is written, including on dry runs.
    """
    if figures is None:
        figures = load_site_figures()
    if slug not in figures:
        return body
    figure = figures[slug]
    matches = list(re.finditer(r"```mermaid[^\S\n]*\n(.*?)```", body, re.S))
    if len(matches) != 1 or matches[0].group(1).strip() != figure["source"]:
        raise ValueError(f"{slug}: source diagram changed; review data/research before importing")
    match = matches[0]
    return body[:match.start()] + figure["shortcode"] + body[match.end():]


WIKILINK = re.compile(r"\[\[([^\[\]|]+?)(?:\|([^\[\]|]+?))?\]\]")

def resolve_wikilinks(body, pages, where):
    """Rewrite Obsidian [[wikilinks]] as markdown links into /research/.

    The vault keeps wikilinks because Obsidian needs them; Hugo has no idea what
    they are and Goldmark passes them straight through as literal text. Before
    this existed, /research shipped 75 of them rendered as "[[The Book Problem]]".

    This has to happen to the markdown rather than in the layout, because
    .Content feeds surfaces a layout never touches: the RSS feed, the meta and
    OpenGraph descriptions, and the JSON-LD articleBody. Fixing only the rendered
    body leaves literal brackets in every link preview and every feed reader.

    Targets resolve on page title, which for this set equals the vault filename.
    An unresolved link is left alone and reported -- loudly, because shipping it
    silently is how the original bug survived a design pass.
    """
    def sub(m):
        target = m.group(1).strip()
        display = (m.group(2) or m.group(1)).strip()
        page = pages.get(target)
        if not page:
            print(f"   ! unresolved wikilink in {where}: {m.group(0)}")
            return m.group(0)
        return f"[{display}](/research/{page['slug']}/)"
    return WIKILINK.sub(sub, body)

def strip_page_frontmatter_artifacts(body):
    # the H1 is redundant with the title, and the short version is lifted into front matter
    body = body.lstrip()
    body = re.sub(r"^# .+\n+", "", body, count=1)
    body = re.sub(r"^> \*\*The short version\*\*.*?\n+", "", body, count=1, flags=re.S | re.M)
    body = re.sub(r"^-{3,}\s*\n+", "", body.lstrip(), count=1)
    return body.lstrip()

if __name__ == "__main__":
    main()
