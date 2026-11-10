#!/usr/bin/env python3
"""Flag headings removed or renamed since a git ref that CHANGELOG.md does not mention.

Usage: python3 docs/maintaining/scripts/check_headings.py [ref]   (default: HEAD)
Run from the repository root. Exits 1 if any removed heading is unrecorded. A removed or moved file counts as recorded when the changelog names its old path.
"""
import re, subprocess, sys

ref = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
base = "docs/guidelines"
files = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, base], capture_output=True, text=True, check=True).stdout.split()
changelog = open(f"{base}/CHANGELOG.md").read().lower()
missing = 0
for f in files:
    if not f.endswith(".md") or f.endswith("CHANGELOG.md"):
        continue
    old = subprocess.run(["git", "show", f"{ref}:{f}"], capture_output=True, text=True, check=True).stdout
    try:
        new = open(f).read()
    except FileNotFoundError:
        new = ""
        if f[len(base) + 1:].lower() in changelog:
            continue
    old_h = set(re.findall(r"^#{2,3}\s+(.*)$", old, re.M))
    new_h = set(re.findall(r"^#{2,3}\s+(.*)$", new, re.M))
    for h in sorted(old_h - new_h):
        if h.lower() not in changelog:
            print(f"UNRECORDED {f}: {h}"); missing += 1
print("unrecorded:", missing)
sys.exit(1 if missing else 0)
