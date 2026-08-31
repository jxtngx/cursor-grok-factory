# Run Ticket Plan

After spec approval. Scrum Master.

## MUST

- Grok inference client + env ticket (skip only if `cursor-only`)
- Cursor SDK client + Grok catalog pick (skip only if `grok-only`)
- On `together`: a ticket that wires **shared session / LangSmith parent trace** across both clients
- Knowledge adapter if not `none`
- LangSmith tracing smoke covering whichever clients are enabled
- Harbor knobs wiring

## MUST NOT

- One ticket for "the whole agent"
- Ship together-mode with only one client
