#!/usr/bin/env python3
"""Check that relative links and heading anchors inside docs/guidelines resolve.

Usage: python3 docs/maintaining/scripts/validate_links.py [path-to-guidelines]
Exits 1 if any link is broken.
"""
import glob, os, re, sys

root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "..", "guidelines")
os.chdir(root)


def slug(h):
    return re.sub(r"\s", "-", re.sub(r"[^\w\s-]", "", h.lower().strip()))


heads = {f: {slug(m.group(1)) for m in re.finditer(r"^#+\s+(.*)$", open(f).read(), re.M)}
         for f in glob.glob("**/*.md", recursive=True)}
bad = 0
for f in heads:
    text = re.sub(r"```.*?```", "", open(f).read(), flags=re.S)
    for m in re.finditer(r"\]\(([^)]+)\)", text):
        link = m.group(1)
        if re.match(r"[a-z]+:", link):
            continue
        path, _, anchor = link.partition("#")
        target = os.path.normpath(os.path.join(os.path.dirname(f), path)) if path else f
        if path and not os.path.exists(target):
            print("MISSING", f, link); bad += 1
        elif anchor and target in heads and anchor not in heads[target]:
            print("ANCHOR", f, link); bad += 1
print("broken links:", bad)
sys.exit(1 if bad else 0)
