---
id: 0000
title: <short title>
stage: architect           # architect | red | green | refactor | explainer | adr-draft | pr-draft
date: YYYY-MM-DD
surface: cursor-composer   # cursor-inline | cursor-chat | cursor-composer | codex-cloud | codex-cli
model: gpt-5-codex
repo_ref: <branch or commit>
scope_files: []            # ["path/one.py", "tests/test_x.py"]
links:
  adr: null
  issue: null
  pr: null
acceptance: []             # Given/When/Then bullets
constraints:
  - minimal diff, no new deps
  - offline tests (mocks)
out_of_scope: []
secrets_policy: "No secrets; use .env"
labels: []                 # ["api", "streaming", "guardrails"]
---

<PASTE THE EXACT PROMPT YOU USED>

### Outcome (fill after run)
- Files changed: ...
- Tests added: ...
- Next prompts: ...
- Notes: ...
