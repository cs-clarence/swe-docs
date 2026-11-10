#!/usr/bin/env python3
"""Regenerate the "Checks per file" table in reviewing/by-tier.md from the checks files.

Usage: python3 docs/maintaining/scripts/by_tier.py [path-to-guidelines]
"""
import glob, os, re, sys

root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "..", "guidelines")
os.chdir(root)
rows = []
for f in sorted(glob.glob("reviewing/checks/**/*.md", recursive=True), key=lambda p: os.path.basename(p)):
    counts = {"Low": 0, "Medium": 0, "High": 0}
    for line in open(f):
        m = re.match(r"\|.*\|\s*(Low|Medium|High)\s*\|\s*$", line)
        if m:
            counts[m.group(1)] += 1
    link = os.path.relpath(f, "reviewing")
    rows.append(f"| [{os.path.basename(f)[:-3]}]({link}) | {counts['Low']} | {counts['Medium']} | {counts['High']} |\n")
head = "| File | Low | Medium | High |\n| --- | --- | --- | --- |\n"
s = open("reviewing/by-tier.md").read()
s = re.sub(r"\| File \| Low \| Medium \| High \|\n.*?(?=\n\n|\Z)", (head + "".join(rows)).rstrip("\n"), s, flags=re.S)
open("reviewing/by-tier.md", "w").write(s)
print("checks files:", len(rows))
