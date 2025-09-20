#!/usr/bin/env python3
import argparse, pathlib, re

parser = argparse.ArgumentParser()
parser.add_argument("--dir", required=True)
args = parser.parse_args()
root = pathlib.Path(args.dir)
rows = []
for p in sorted(root.glob("*.prompt.md")):
    parts = p.read_text().split("---",2)
    meta = parts[1] if len(parts)>2 else ""
    def get(k):
        m = re.search(rf"\n{k}:\s*(.*)", meta)
        return (m.group(1).strip() if m else "").strip()
    rid = get("id") or p.name[:4]
    title = get("title") or p.stem
    stage = get("stage") or "?"
    date_val = get("date") or ""
    rows.append((rid, title, stage, date_val, p.name))
index = ["# Prompt History Index\n", "| ID | Title | Stage | Date | File |\n", "|---|---|---|---|---|\n"]
for r in rows:
    index.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |\n")
(root/"index.md").write_text("".join(index))
print("Wrote", root/"index.md")
