# Cursor Grok Factory

A **factory**, not a lab.

Boilerplate for a product that uses **Grok** ([xAI API](https://docs.x.ai/overview))
and/or the **[Cursor SDK / APIs](https://cursor.com/docs/api)**.
At `@init-grok` you choose **together**, **Grok-only**, or **Cursor-only**.
Cursor's team implements from a spec you write in the first session.

Sister: [cursor-agent-factory](https://github.com/jxtngx/cursor-agent-factory)
(LangChain-only). This factory is **Grok-first** and lets you pick the Grok
inference SDK. Cursor is the workspace/agent runtime; when you pick together,
it prefers Grok from the catalog.

[LangSmith](https://docs.smith.langchain.com/) is **always on for observability**.
You choose which extra LangSmith pieces to use. [Harbor](https://harborframework.com/)
tunes the harness knobs.

Commanded by [cursor-factory-command](https://github.com/jxtngx/cursor-factory-command).

---

## First command

```
@init-grok
```

1. **Language** — Python or TypeScript (one product)
2. **Grok inference SDK** — one of:
   - [LangChain xAI](https://docs.langchain.com/oss/python/integrations/providers/xai) (`ChatXAI` / `@langchain/xai`)
   - [xAI SDK](https://docs.x.ai/overview) (`xai_sdk` on Python; first-party client on TS)
   - [Vercel AI SDK](https://ai-sdk.dev/providers/ai-sdk-providers/xai) (`@ai-sdk/xai`) — **TypeScript only**
3. **Cursor pairing** — required choice, no default:
   - Together — Grok inference + Cursor agents/workspace
   - Grok-only — no Cursor SDK
   - Cursor-only — Cursor SDK, Grok from the catalog, no direct xAI client
4. **Knowledge** — local files, AWS (S3), or none (chat-session scoped)
5. **LangSmith components** — tracing is locked on; you opt into datasets, evals, prompts, monitoring, annotations
6. Writes requirements + `harness/knobs.yaml` + `TRACK.md`
7. Hands off `@chief-architect` → SME → `@scrum-master` → tickets

Do not ask an engineer to `pip install` a client before the spec exists.

## Opinionated stack (not optional)

| Layer | Choice |
| --- | --- |
| Pairing | Chosen at init: `together` \| `grok-only` \| `cursor-only`. Together is allowed, not assumed. |
| Models | **Grok** (`grok-4.6` on xAI; Cursor catalog Grok 4.6 / Grok 4.5 when Cursor is enabled). No Auto/router unless the spec says so. |
| xAI | [docs.x.ai](https://docs.x.ai/overview) — `XAI_API_KEY` |
| Cursor | [cursor.com/docs/api](https://cursor.com/docs/api) — `CURSOR_API_KEY` |
| Observability | LangSmith **tracing always**, wrapping both clients. Other components from init. |
| Tune | Harbor + `harness/knobs.yaml` (`--plugin langsmith`; `--agent langgraph` on the LangChain track) |
| Knowledge | `local` \| `aws` \| `none` |

Invalid combinations (init must refuse):

- TypeScript + a Python-only package, or Python + Vercel AI SDK
- Two **inference** SDKs in one product (LangChain + xAI SDK + Vercel). Cursor SDK is a separate pairing choice.
- Tracing off
- Cursor Auto as the default model while Grok is in the catalog
- Skipping the pairing question or assuming together

## Tracks (`TRACK.md`)

One line, `{language}-{sdk}`:

| TRACK | Language | SDK |
| --- | --- | --- |
| `python-langchain` | Python | `langchain-xai` |
| `python-xai-sdk` | Python | `xai-sdk` (`xai_sdk.Client`) |
| `typescript-langchain` | TypeScript | `@langchain/xai` |
| `typescript-xai-sdk` | TypeScript | xAI first-party / REST client |
| `typescript-vercel-ai` | TypeScript | `ai` + `@ai-sdk/xai` |

Knowledge is a knob, not a track: `harness/knobs.yaml` → `knowledge.kind`.
Cursor pairing is a knob set at init: `harness/knobs.yaml` → `cursor.pairing` (`together` \| `grok-only` \| `cursor-only`).

## Team

| Agent | Job |
| --- | --- |
| Product Manager | `@init-grok` / `@launch-product-discovery` |
| Chief Architect | Track fit, Grok+Cursor pairing, knowledge boundary |
| Grok SME | xAI models, Responses API, Cursor Grok IDs, how the two clients share a session |
| LangChain SME | `ChatXAI` / `@langchain/xai` (LangChain track only) |
| Cursor SDK SME | [Python](https://cursor.com/docs/sdk/python) / [TS](https://cursor.com/docs/sdk/typescript) agents, local vs cloud |
| Scrum Master | Sprint + tickets |
| Agent Engineer | Implements the client(s) the pairing named |
| Eval Engineer | LangSmith + Harbor |
| Test Developer | Fake-model tests; no live keys in CI |

## Daily loop

```
@init-grok  →  approve spec  →  tickets  →  @tune-harness
```
