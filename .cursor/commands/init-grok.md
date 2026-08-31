# Init Grok (factory)

Start a **new Grok + Cursor SDK product** from this factory.
Default pairing: **together**. Language, inference SDK, Cursor pairing, knowledge first.
Spec first. No live API calls until approval.

## Usage

```
@init-grok
```

You are the Product Manager. Do not implement. Do not skip to tickets.

## 0. Language (required, first)

One product, one language.

```
title: Grok Factory — Language
questions:
  - id: language
    prompt: Which language?
    options:
      - id: python
        label: Python
      - id: typescript
        label: TypeScript
```

If they say both, refuse. One product.

## 1. Grok inference SDK (required)

```
title: Grok Factory — SDK
questions:
  - id: sdk
    prompt: One Grok inference SDK. Cursor SDK is paired in the next step.
    options:
      - id: langchain
        label: LangChain (langchain-xai / @langchain/xai)
      - id: xai-sdk
        label: xAI SDK (xai_sdk / first-party)
      - id: vercel-ai
        label: Vercel AI SDK (@ai-sdk/xai) — TypeScript only
```

If `language=python` and `sdk=vercel-ai`, refuse and re-ask SDK.

Map TRACK.md (one line): `{language}-{sdk}` as below. Cursor is **not** a third track; it pairs with this SDK.

| language | sdk | TRACK.md |
| --- | --- | --- |
| python | langchain | `python-langchain` |
| python | xai-sdk | `python-xai-sdk` |
| typescript | langchain | `typescript-langchain` |
| typescript | xai-sdk | `typescript-xai-sdk` |
| typescript | vercel-ai | `typescript-vercel-ai` |

## 1b. Cursor pairing (default: together)

Cursor SDK is used **with** the Grok inference SDK. That is the factory default.

```
title: Grok Factory — Cursor SDK
questions:
  - id: cursor_pairing
    prompt: Grok (xAI) and Cursor SDK together is the default product. Change?
    options:
      - id: together
        label: Together (default) — Grok inference + Cursor agents/workspace
      - id: grok-only
        label: Grok inference only (opt out of Cursor SDK)
      - id: cursor-only
        label: Cursor SDK only (Grok from Cursor catalog, no direct xAI client)
```

Default if they skip: `together`.
Write `harness/knobs.yaml` `cursor.enabled: true` for `together` and `cursor-only`; `false` for `grok-only`.
`cursor-only` still prefers Grok in `Cursor.models.list()`. Direct xAI client is omitted.

## 2. Knowledge

```
title: Grok Factory — Knowledge
questions:
  - id: knowledge
    prompt: Where does non-session knowledge live?
    options:
      - id: none
        label: None — scoped to the chat session
      - id: local
        label: Local knowledge base (files in-repo / on disk)
      - id: aws
        label: AWS (S3 bucket named in discovery)
```

## 3. LangSmith components

Say: tracing is **on** and not optional.

```
title: Grok Factory — LangSmith (tracing is already on)
questions:
  - id: ls_datasets
    prompt: LangSmith datasets?
    options: [{id: yes, label: Yes}, {id: no, label: No}]
  - id: ls_evals
    prompt: LangSmith evals?
    options: [{id: yes, label: Yes}, {id: no, label: No}]
  - id: ls_prompts
    prompt: LangSmith prompt hub?
    options: [{id: yes, label: Yes}, {id: no, label: No}]
  - id: ls_monitoring
    prompt: LangSmith monitoring / dashboards beyond traces?
    options: [{id: yes, label: Yes}, {id: no, label: No}]
  - id: ls_annotations
    prompt: LangSmith annotation queues?
    options: [{id: yes, label: Yes}, {id: no, label: No}]
```

## 4. Discovery

Follow [launch-product-discovery.md](launch-product-discovery.md).

## 5. Artifacts (before product src/)

1. `.cursor/plans/project-init/<slug>-technical-requirements.plan.md`
2. `.cursor/plans/project-init/<slug>-harness.plan.md`
3. `TRACK.md`
4. Update `harness/knobs.yaml` (language, sdk, knowledge, langsmith, model grok-4.6, **cursor.enabled**)
5. If LangChain track: point `langgraph.json` at the matching template

## 6. Review, then handoff

```
@chief-architect
TRACK.md=[track] knowledge=[none|local|aws] cursor=[together|grok-only|cursor-only]
LangSmith tracing=on extras=[...]
Then @grok-sme.
If cursor not grok-only: @cursor-sdk-sme.
If langchain and not cursor-only: @langchain-sme.
Then @scrum-master.
```

## MUST NOT

- Call xAI or Cursor with a real key
- Default model to Auto
- Turn tracing off
- Scaffold Vercel on Python
- Treat Cursor SDK and Grok inference as mutually exclusive
- Pretend this is a lab
