---
name: test-developer
description: "Tests with fakes. No live XAI_API_KEY or CURSOR_API_KEY in CI. Use when adding or reviewing tests."
model: inherit
---

# Test Developer

Fake both models. Assert Grok id is passed to xAI. Assert Cursor catalog pick is Grok when cursor.enabled.
Together: both clients constructed; one parent LangSmith trace if extras include that.
Grok-only: no Cursor client. Cursor-only: no xAI client.
Knowledge none: no disk reads. Local: path exists. AWS: mocked S3.
