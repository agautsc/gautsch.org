#!/usr/bin/env python3
"""Fill in the stamps on /arg-atl-dining/ from a family library's dining record.

    python scripts/publish_dining_stamps.py --library <library folder>           # write stamps.json
    python scripts/publish_dining_stamps.py --library <library folder> --check   # say what it would write
    python scripts/publish_dining_stamps.py --library <library folder> --push    # and publish it

The page is read-only. Its stamps come from static/arg-atl-dining/stamps.json, which this writes:

    {"stamps": {"30": {"date": "2026-11-20", "note": "..."}}}

The library is a Family Library folder (github.com/BearHall/family-library). Each restaurant there is
restaurants/<id>/restaurant.yaml, and each time someone ate there is a `visited` event with its date and what they
said. A restaurant matches a place on the list by its name or its folder id. Its stamp carries the date of the first
visit. What was said is left out unless that visit has `public: true`, which only a person adds; then the newest
such note is shown.

--push is for a folder kept only for this job: it moves the folder to origin/main first, then commits
stamps.json and pushes it when it changed. It refuses when the folder has other changes. --log <file> is for a
run nobody watches (a scheduled task with no window): a change or a failure adds a line to it. Needs PyYAML.
"""
import argparse
import datetime
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import yaml

SITE = Path(__file__).resolve().parent.parent
PAGE = "static/arg-atl-dining/index.html"
OUT = "static/arg-atl-dining/stamps.json"
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}")
ROW = re.compile(r'^\[(\d+),"([^"]+)","([^"]+)",', re.M)   # the page's own list: [rank, name, stamp name, ...
# A name the family might use for a place, when it's neither the list's name nor the one on its stamp.
ALSO = {5: ["season"], 7: ["pink-lotus-thai"], 11: ["charm-thai"], 12: ["weepa"], 14: ["deer-and-dove"],
        16: ["sugar-loaf-bakery", "sugar-loaf-bakery-and-cafe"], 18: ["kamayan"], 19: ["enzo-steakhouse"],
        20: ["porter-beer-bar", "the-porter"], 22: ["chastain"], 32: ["bey-mediterranean", "bey-mediterranean-kitchen"],
        34: ["jds", "jds-summerhill-deli"], 40: ["consulate"], 42: ["spring", "spring-second-branch"],
        43: ["hen-mother"], 46: ["bertolozis", "bertolozis-pizza"], 48: ["twisted-soul-cookhouse"]}


def slug(text):
    text = unicodedata.normalize("NFKD", str(text)).encode("ascii", "ignore").decode().lower()
    text = text.replace("&", " and ").replace("+", " and ").replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def places(page):
    """{a name's slug: rank} for the fifty places, read from the page so the two can't drift apart."""
    found = {}
    rows = ROW.findall(Path(page).read_text(encoding="utf-8"))
    if len(rows) != 50:
        raise SystemExit(f"{page}: expected the list's 50 places, found {len(rows)}")
    for rank, name, short in rows:
        for key in (slug(name), slug(short), *ALSO.get(int(rank), [])):
            if found.setdefault(key, int(rank)) != int(rank):
                raise SystemExit(f"{key!r} names two places on the list: {found[key]} and {rank}")
    return found


def stamps(library, ranks):
    """({rank: {date, note?}}, [restaurants in the library that aren't on the list])."""
    out, others = {}, []
    for record in sorted(Path(library).glob("restaurants/*/restaurant.yaml")):
        data = yaml.safe_load(record.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("archived"):
            continue
        rank = ranks.get(slug(record.parent.name)) or ranks.get(slug(data.get("name") or ""))
        if not rank:
            others.append(record.parent.name)
            continue
        visits = sorted((str(e["date"]), e) for e in data.get("events") or []
                        if isinstance(e, dict) and e.get("what") == "visited" and not e.get("undone")
                        and DATE.match(str(e.get("date") or "")))
        if not visits:
            continue
        stamp = {"date": visits[0][0][:10]}
        shared = [e["note"].strip() for _, e in visits
                  if e.get("public") is True and isinstance(e.get("note"), str) and e["note"].strip()]
        if shared:
            stamp["note"] = shared[-1]
        if rank in out and out[rank]["date"] <= stamp["date"]:
            continue   # two records for one place: the earlier first visit is the stamp
        out[rank] = stamp
    return out, others


def git(site, *args, check=True):
    done = subprocess.run(["git", "-C", str(site), *args], capture_output=True, text=True, encoding="utf-8")
    if check and done.returncode:
        raise SystemExit(f"git {' '.join(args)}: {done.stderr.strip() or done.stdout.strip()}")
    return done.stdout.strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--library", required=True, help="the family library folder")
    parser.add_argument("--site", default=SITE, type=Path, help="this repository (default: where this script is)")
    parser.add_argument("--check", action="store_true", help="print what would be written, and write nothing")
    parser.add_argument("--push", action="store_true", help="move to origin/main, then commit and push a change")
    parser.add_argument("--log", type=Path, help="add a line to this file when something changed or failed")
    args = parser.parse_args()
    failed = False
    try:
        said = run(args)
    except (OSError, yaml.YAMLError) as error:   # a record half written: publish nothing, try again next time
        said, failed = [f"nothing published: {error}"], True
    except SystemExit as stop:
        if not isinstance(stop.code, str):
            raise
        said, failed = [stop.code], True
    print("\n".join(said))
    if args.log and (failed or "no change" not in said) and not args.check:
        args.log.parent.mkdir(parents=True, exist_ok=True)
        with open(args.log, "a", encoding="utf-8") as log:
            log.write(f"{datetime.datetime.now():%Y-%m-%d %H:%M} {'; '.join(said)}\n")
    sys.exit(1 if failed else 0)


def run(args):
    """Do it, and return what to say, a line each."""
    if not (Path(args.library) / "README.md").is_file():
        raise SystemExit(f"{args.library} isn't a library folder (no README.md)")
    if args.push and not args.check:
        other = [line for line in git(args.site, "status", "--porcelain").splitlines() if not line.endswith(OUT)]
        if other:
            raise SystemExit("this folder has other changes, so nothing was published: " + ", ".join(other))
        git(args.site, "fetch", "--quiet", "origin", "main")
        git(args.site, "checkout", "--quiet", "--detach", "origin/main")
    found, others = stamps(args.library, places(args.site / PAGE))
    text = json.dumps({"stamps": {str(k): found[k] for k in sorted(found)}}, ensure_ascii=False, indent=1) + "\n"
    target = args.site / OUT
    said = [f"{len(found)} stamped" + (f"; not on the list: {', '.join(others)}" if others else "")]
    if args.check:
        return [*said, text.rstrip("\n")]
    if target.is_file() and target.read_text(encoding="utf-8") == text:
        return [*said, "no change"]
    target.write_text(text, encoding="utf-8", newline="\n")
    said.append(f"wrote {OUT}")
    if args.push:
        git(args.site, "add", OUT)
        git(args.site, "commit", "--quiet", "-m", f"Dining passport: {len(found)} of 50 stamped")
        git(args.site, "push", "--quiet", "origin", "HEAD:main")
        said.append("pushed " + git(args.site, "rev-parse", "--short", "HEAD"))
    return said


if __name__ == "__main__":
    main()
