# Harness

`knobs.yaml` is the parameter file [Harbor](https://harborframework.com/) and LangSmith sweep.

| Track | Harbor |
| --- | --- |
| `*-langchain` | `--agent langgraph --plugin langsmith` |
| `*-xai-sdk` / `typescript-vercel-ai` | custom runner reading this YAML; still `--plugin langsmith` |

Model id stays a Grok id.
