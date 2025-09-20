#!/usr/bin/env python3
import argparse, pathlib, re, datetime

TPL = """---
id: {id}
title: {title}
stage: {stage}
date: {date}
surface: cursor-composer
model: gpt-5-codex
repo_ref: <branch-or-commit>
scope_files: []
links:
  adr: null
  issue: null
  pr: null
acceptance: []
constraints:
  - minimal diff, no new deps
  - offline tests (mocks)
out_of_scope: []
secrets_policy: "No secrets; use .env"
labels: []
---

<PASTE THE EXACT PROMPT YOU USED>

### Outcome
- Files changed: 
- Tests added: 
- Next prompts: 
- Notes: 
"""

def next_id(dir: pathlib.Path) -> int:
    ids = []
    for p in dir.glob("*.prompt.md"):
        m = re.match(r"(\d{4})-", p.name)
        if m:
            ids.append(int(m.group(1)))
    return max(ids) + 1 if ids else 1

parser = argparse.ArgumentParser()
parser.add_argument("--dir", required=True)
parser.add_argument("--slug", required=True)
parser.add_argument("--stage", required=True, choices=["architect","red","green","refactor","explainer","adr-draft","pr-draft"])
parser.add_argument("--title", default=None)
args = parser.parse_args()

root = pathlib.Path(args.dir)
root.mkdir(parents=True, exist_ok=True)
_id = next_id(root)
id_str = f"{_id:04d}"
slug = re.sub(r"[^a-z0-9-]","-", args.slug.lower())
fn = root / f"{id_str}-{slug}-{args.stage}.prompt.md"

content = TPL.format(
    id=id_str,
    title=(args.title or args.slug.replace("-"," ")).title(),
    stage=args.stage,
    date=datetime.date.today().isoformat(),
)
fn.write_text(content)
print(str(fn))
