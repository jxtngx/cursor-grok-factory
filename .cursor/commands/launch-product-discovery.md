# Launch Product Discovery

After language, Grok SDK, Cursor pairing, and knowledge are locked. Spec only.

## MUST cover

- Job the product does (one sentence)
- How Grok inference and Cursor SDK **share work** (default: together)
  - Grok/xAI: chat, tools, Responses API
  - Cursor SDK: local/cloud agents, workspace edits, Grok from the catalog
  - One LangSmith project traces both
- If grok-only or cursor-only, why the other client is absent
- Tools the Grok agent may call
- Cursor runtime: local, cloud, or both
- Knowledge: if local, path and file types; if aws, bucket + prefix + region; if none, confirm session-only
- LangSmith extras already chosen
- Harbor: what knobs to sweep (prompt, tools, temperature)
- Falsifier

Write the two plan files from templates.

## MUST NOT

- Implement
- Add a second **inference** SDK
- Force the user to pick Grok *or* Cursor
