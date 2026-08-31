# Launch Product Discovery

After language, Grok SDK, Cursor pairing, and knowledge are locked. Spec only.

## MUST cover

- Job the product does (one sentence)
- How Grok inference and Cursor SDK relate, using the pairing they **already chose** (`together` | `grok-only` | `cursor-only`)
  - Together: Grok/xAI chat+tools; Cursor SDK local/cloud agents; one LangSmith project
  - Grok-only / cursor-only: do not add the other client
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
- Change the pairing they locked at init

