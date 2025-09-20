---
id: 0002
title: Hello World
stage: red
date: 2025-09-20
surface: cursor-composer
model: gpt-5-codex
repo_ref: <branch-or-commit>
scope_files: []
links:
  adr: {previous_prompt: 0001}
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

Add failing tests for /hello. No production code! Use pytest and FastAPI TestClient. Test: GET /hello returns 200 JSON {"message": "Hello World!"}. Offline mocks. Per PHR-0001.


### Outcome
- Files changed: tests/test_hello.py (added comprehensive failing tests)
- Tests added: 6 new failing tests demonstrating RED phase of TDD
- Next prompts: Ready for GREEN phase implementation
- Notes: 5 tests fail, 9 tests pass - demonstrates proper TDD red phase with failing tests for future features 
