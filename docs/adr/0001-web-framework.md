# ADR-0001: Choose Web Framework for Hello App

- **Status:** Accepted
- **Date:** 2025-09-20

## Context
Need a simple API for /hello endpoint. Async support for future agentic features like real-time responses.

## Options
- A) Flask: Basic and quick. Pros: Minimal. Cons: Limited async.
- B) FastAPI: Modern with auto-docs. Pros: Type-safe, async-ready for AI. Cons: Small setup.
- C) No framework: Custom HTTP. Pros: Ultra-light. Cons: Reinvents basics.

## Decision
Choose FastAPI—suits Python agentic AI with validation and speed.

## Consequences
- Positive: Easy to extend for agents; built-in testing.
- Negative: Adds deps (managed by uv).
- References: uv docs for setup.