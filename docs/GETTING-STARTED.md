# Getting started

Keys live in env. Copy `.env.example`. Do not commit `.env`.

```
@init-grok
```

Official:

- https://docs.x.ai/overview
- https://cursor.com/docs/api
- https://cursor.com/docs/sdk/python
- https://cursor.com/docs/sdk/typescript
- https://docs.langchain.com/oss/python/integrations/providers/xai
- https://ai-sdk.dev/providers/ai-sdk-providers/xai
- https://docs.smith.langchain.com/

Together-mode needs both keys. Grok-only omits Cursor. Cursor-only omits xAI.

Grok on xAI needs `XAI_API_KEY`.
Cursor SDK needs `CURSOR_API_KEY`.
LangSmith tracing needs `LANGCHAIN_API_KEY` (or `LANGSMITH_API_KEY`).

