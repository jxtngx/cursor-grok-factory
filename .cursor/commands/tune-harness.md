# Tune Harness

Harbor + LangSmith. Eval Engineer.

## Usage

```
@tune-harness
```

## MUST

- Read `harness/knobs.yaml`
- LangChain track: Harbor `--agent langgraph --plugin langsmith`
- Other tracks: Harbor trial overrides knobs (model, prompt, tools) via env/config; do not invent a second YAML
- Model id stays a Grok id unless the user explicitly sweeps non-Grok (refuse by default)
- Tracing stays on for every trial

## MUST NOT

- Sweep in a live production key from chat
- Disable LangSmith to "go faster"
