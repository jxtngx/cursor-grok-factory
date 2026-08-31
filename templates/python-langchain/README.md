# Track: python-langchain

Walking skeleton. Do not copy into a product tree until the spec is approved.

If `cursor.pairing: together`:

- `langchain-xai` `ChatXAI(model="grok-4.6")` — inference
- `cursor-sdk` — `Agent.create`, Grok from `Cursor.models.list()`
- Shared LangSmith parent trace
- LangGraph `make_graph` reads `harness/knobs.yaml`

`grok-only`: omit Cursor. `cursor-only`: omit ChatXAI.
