# Track: python-langchain

Walking skeleton. Do not copy into a product tree until the spec is approved.

Together (default):

- `langchain-xai` `ChatXAI(model="grok-4.6")` — inference
- `cursor-sdk` — `Agent.create`, Grok from `Cursor.models.list()`
- Shared LangSmith parent trace
- LangGraph `make_graph` reads `harness/knobs.yaml`

Opt-out: omit Cursor if `cursor.pairing: grok-only`; omit ChatXAI if `cursor-only`.
