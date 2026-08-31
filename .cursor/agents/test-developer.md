---
name: test-developer
description: "Tests with fakes. No live XAI_API_KEY in CI. Use when adding or reviewing tests."
model: inherit
---

# Test Developer

Fake the model. Assert Grok id is passed. Assert tracing env is set.
Knowledge none: no disk reads. Local: path exists. AWS: mocked S3.
