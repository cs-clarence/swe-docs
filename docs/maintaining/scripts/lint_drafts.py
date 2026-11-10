#!/usr/bin/env python3
"""Check draft hygiene in docs/guidelines.

Reports: an authoring file with no checks file, a file missing from its area README,
and (with --release) any remaining draft banner or marker.

Usage: python3 docs/maintaining/scripts/lint_drafts.py [--release] [path-to-guidelines]
"""
import glob, os, sys

args = [a for a in sys.argv[1:] if not a.startswith("--")]
release = "--release" in sys.argv
root = args[0] if args else os.path.join(os.path.dirname(__file__), "..", "..", "guidelines")
os.chdir(root)
bad = 0
for f in sorted(glob.glob("authoring/**/*.md", recursive=True)):
    n = os.path.basename(f)
    if n in ("README.md", "agents.md"):
        continue
    if not os.path.exists("reviewing/checks/" + f[len("authoring/"):]):
        print("NO CHECKS", f); bad += 1
for readme_path in sorted(glob.glob("*/README.md") + glob.glob("authoring/*/README.md")):
    d = os.path.dirname(readme_path)
    readme = open(readme_path).read()
    for f in glob.glob(f"{d}/*.md"):
        n = os.path.basename(f)
        if n != "README.md" and f"({n})" not in readme:
            print("NOT INDEXED", f); bad += 1
    for sub in glob.glob(f"{d}/*/README.md"):
        g = os.path.basename(os.path.dirname(sub))
        if f"({g}/README.md)" not in readme:
            print("NOT INDEXED", sub); bad += 1
if release:
    for f in glob.glob("**/*.md", recursive=True):
        s = open(f).read()
        if "> **Draft.**" in s or "*(draft)*" in s:
            print("DRAFT LEFT", f); bad += 1
print("problems:", bad)
sys.exit(1 if bad else 0)
