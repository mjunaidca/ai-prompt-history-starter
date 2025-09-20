---
id: 0001
title: Plan Hello World Endpoint
stage: architect
date: 2025-09-20
surface: cursor-composer
model: gpt-5-codex
repo_ref: <branch-or-commit>
scope_files: ["app/main.py", "tests/test_hello.py"]
links:
  adr: docs/adr/0001-web-framework.md
  issue: null
  pr: null
acceptance: ["GET /hello returns 200 JSON {'message': 'Hello World!'}"]
constraints:
  - minimal diff, no new deps
  - offline tests (mocks)
out_of_scope: []
secrets_policy: "No secrets; use .env"
labels: []
---

You are the architect. Plan a FastAPI app with /hello endpoint. Per ADR-0001, use FastAPI. Files: app/main.py. Acceptance: GET /hello -> 200 JSON {"message": "Hello World!"}. Constraints: Minimal diff, no extra deps beyond FastAPI.

### Outcome
- Files changed: 
- Tests added: 
- Next prompts: 
- Notes: 
