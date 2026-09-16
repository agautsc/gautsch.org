#!/usr/bin/env python3
"""Check a built gautsch.org site before it is published.

    hugo --minify -d public && python3 scripts/check_site.py public

Fails (exit 1) on: broken internal links or assets, unresolved Obsidian [[links]]
in rendered pages, a missing or unreadable reading pack for any rabbit hole,
feeds or JSON-LD that do not parse, and year-0001 dates. Standard library only,
so CI needs nothing beyond Python. Run by .github/workflows/validate.yml and
before every deploy in hugo.yml.
"""
import glob
import json
import os
import re
import sys
import xml.dom.minidom
from urllib.parse import unquote, urlparse

SITE_HOST = "gautsch.org"


def main(root):
    root = os.path.abspath(root)
    problems = []

    def exists(path):
        path = unquote(path.split("#")[0].split("?")[0])
        full = os.path.join(root, path.lstrip("/"))
        return (os.path.isfile(full) or os.path.isfile(os.path.join(full, "index.html"))
                or os.path.isfile(full.rstrip("/") + "/index.html"))

    pages = glob.glob(os.path.join(root, "**", "*.html"), recursive=True)
    for page in pages:
        rel = "/" + os.path.relpath(page, root)
        html = open(page, encoding="utf-8").read()
        if "http-equiv=refresh" in html or 'http-equiv="refresh"' in html:
            continue
        body = re.sub(r"(?is)<(script|style|textarea)\b.*?</\1>", "", html)
        if "[[" in body:
            problems.append(f"{rel}: unresolved [[ markup")
        if "0001-01-01" in html:
            problems.append(f"{rel}: year-0001 date")
        for url in re.findall(r'(?:href|src)=["\']?([^"\'\s>]+)', html):
            parsed = urlparse(url)
            if parsed.scheme in ("mailto", "tel", "data", "javascript"):
                continue
            if parsed.netloc and parsed.netloc != SITE_HOST:
                continue
            path = parsed.path
            if not path:
                continue
            if not path.startswith("/"):
                path = os.path.join(os.path.dirname(rel), path)
            if not exists(path):
                problems.append(f"{rel}: broken internal link {url}")
        for block in re.findall(r'(?s)<script type=["\']?application/ld\+json["\']?>(.*?)</script>', html):
            try:
                json.loads(block)
            except ValueError as err:
                problems.append(f"{rel}: JSON-LD does not parse ({err})")

    holes = [d for d in glob.glob(os.path.join(root, "research", "*", "index.html"))]
    if len(holes) < 1:
        problems.append("research: no rabbit-hole pages were built")
    for hole in holes:
        folder = os.path.dirname(hole)
        for pack in ("reading-pack.md", "reading-pack.html"):
            path = os.path.join(folder, pack)
            if not os.path.isfile(path) or os.path.getsize(path) < 500:
                problems.append(f"{os.path.relpath(path, root)}: missing or empty reading pack")

    for feed in glob.glob(os.path.join(root, "**", "index.xml"), recursive=True) + [os.path.join(root, "sitemap.xml")]:
        try:
            xml.dom.minidom.parse(feed)
        except Exception as err:  # noqa: BLE001 - report any parse failure
            problems.append(f"{os.path.relpath(feed, root)}: does not parse ({err})")

    for name in ("robots.txt", "llms.txt"):
        if not os.path.isfile(os.path.join(root, name)):
            problems.append(f"{name}: missing")

    unique = sorted(set(problems))
    for line in unique[:200]:
        print(line)
    print(f"checked {len(pages)} HTML files and {len(holes)} rabbit holes: {len(unique)} problem(s)")
    return 1 if unique else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "public"))
