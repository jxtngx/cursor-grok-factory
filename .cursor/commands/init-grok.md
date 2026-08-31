# Init Grok (factory)

Start a **new Grok + Cursor SDK product** from this factory.
Language, SDK, knowledge first. Spec first. No live API calls until approval.

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

## 1. SDK (required)

```
title: Grok Factory — SDK
questions:
  - id: sdk
    prompt: One SDK. Grok models on all of them.
    options:
      - id: langchain
        label: LangChain (langchain-xai / @langchain/xai)
      - id: xai-sdk
        label: xAI SDK (xai_sdk / first-party)
      - id: vercel-ai
        label: Vercel AI SDK (@ai-sdk/xai) — TypeScript only
```

If `language=python` and `sdk=vercel-ai`, refuse and re-ask SDK.

Map TRACK.md (one line):

| language | sdk | TRACK.md |
| --- | --- | --- |
| python | langchain | `python-langchain` |
| python | xai-sdk | `python-xai-sdk` |
| typescript | langchain | `typescript-langchain` |
| typescript | xai-sdk | `typescript-xai-sdk` |
| typescript | vercel-ai | `typescript-vercel-ai` |

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
4. Update `harness/knobs.yaml` (language, sdk, knowledge, langsmith, model grok-4.6)
5. If LangChain track: point `langgraph.json` at the matching template

## 6. Review, then handoff

```
@chief-architect
TRACK.md=[track] knowledge=[none|local|aws]
LangSmith tracing=on extras=[...]
Then @grok-sme.
If langchain: @langchain-sme.
Then @scrum-master.
```

## MUST NOT

- Call xAI or Cursor with a real key
- Default model to Auto
- Turn tracing off
- Scaffold Vercel on Python
- Pretend this is a lab
