# AGENTS.md — Cursor Grok Factory

This repository is a **factory**, not a lab.

Canonical contract: [cursor-langchain-factory](https://github.com/jxtngx/cursor-langchain-factory).

> **Lab** = the human writes the code.
> **Factory** = the human defines requirements. This team ships tickets.

## Before the spec

Only `@init-grok` / `@launch-product-discovery`.
No client constructors, no live `XAI_API_KEY` calls.

## After the spec is approved

Engineers implement the ticket. Do not send the Product Owner to write `ChatXAI` themselves.

## Stack

- Grok models preferred. Cursor SDK uses Grok from the catalog, not Auto, unless the spec opts in.
- One language. One **inference** SDK track. Cursor pairing (`together` | `grok-only` | `cursor-only`) is chosen at init.
- LangSmith tracing always (`LANGSMITH_TRACING` / `LANGCHAIN_TRACING_V2`), covering both clients.
- Harbor reads `harness/knobs.yaml`.
- Official docs: [docs.x.ai](https://docs.x.ai/overview), [cursor.com/docs/api](https://cursor.com/docs/api), [LangChain xAI](https://docs.langchain.com/oss/python/integrations/providers/xai).
- No secrets in git.

## Markdown

No emojis. One sentence per line.
