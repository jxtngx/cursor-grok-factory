"""Harbor / LangGraph entry. Engineers replace this after spec approval.

Honor cursor.pairing from knobs: together ships ChatXAI plus cursor-sdk;
grok-only / cursor-only ship one client.
"""


def make_graph(config: dict | None = None):
    raise NotImplementedError(
        "cursor-grok-factory: implement after TRACK.md is python-langchain and the spec is approved"
    )
