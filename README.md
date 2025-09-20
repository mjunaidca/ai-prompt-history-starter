# AI Prompt History Starter

A minimal repository skeleton that treats prompts as first-class artifacts alongside ADRs.
Generated: 2025-09-20

## Quick start
```bash
git init
git config core.hooksPath .githooks
chmod +x .githooks/*
chmod +x scripts/*.py
make prompt-new SLUG=hello-world STAGE=architect
make prompt-index
```

## Layout
- docs/adr/ — Architecture Decision Records
- docs/prompts/ — Prompt History Records (PHR-####)
- scripts/ — helper scripts
- .githooks/ — pre-commit & commit-msg hooks
