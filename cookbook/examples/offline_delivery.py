"""Synthetic engineering exercise; no LLM, network or production integration."""
import json
from pathlib import Path


def retrieve(documents, tenant, query):
    visible = [d for d in documents if d["tenant"] == tenant and d["active"]]
    ranked = [(sum(term in query for term in d["terms"]), d) for d in visible]
    ranked.sort(key=lambda item: (-item[0], item[1]["id"]))
    if not ranked or ranked[0][0] == 0:
        return {"answer": None, "citation": None, "status": "abstain"}
    doc = ranked[0][1]
    return {"answer": doc["text"], "citation": doc["id"], "status": "evidence"}


class SandboxTool:
    """Process-local idempotency example, not a durable production service."""

    def __init__(self):
        self.results = {}
        self.effects = []

    def create_draft(self, identity, tenant, request_id, text):
        if identity != tenant or tenant not in {"alpha", "beta"}:
            raise PermissionError("FORBIDDEN")
        if not request_id or not text:
            raise ValueError("INVALID_INPUT")
        key = (tenant, request_id)
        if key in self.results:
            previous_text, result = self.results[key]
            if previous_text != text:
                raise ValueError("IDEMPOTENCY_CONFLICT")
            return result
        result = {"draft_id": len(self.effects) + 1, "status": "needs_review"}
        self.effects.append((tenant, text))
        self.results[key] = (text, result)
        return result


def main():
    fixture = json.loads(Path(__file__).with_name("fixtures.json").read_text())
    assert fixture["synthetic"] is True
    checks = []
    for query in fixture["queries"]:
        result = retrieve(fixture["documents"], query["tenant"], query["query"])
        assert result["citation"] == query["expected"], query["id"]
        checks.append(query["id"])
    tool = SandboxTool()
    first = tool.create_draft("alpha", "alpha", "r1", "合成答复草稿")
    assert tool.create_draft("alpha", "alpha", "r1", "合成答复草稿") == first
    assert len(tool.effects) == 1
    checks.append("idempotent-retry")
    for args, error in [
        (("beta", "alpha", "r2", "forbidden"), PermissionError),
        (("alpha", "alpha", "r1", "changed"), ValueError),
    ]:
        try:
            tool.create_draft(*args)
        except error:
            checks.append(error.__name__)
        else:
            raise AssertionError("Expected rejection")
    assert len(tool.effects) == 1
    print(json.dumps({"synthetic": True, "passed": len(checks),
                      "checks": checks, "production_ready": False}, ensure_ascii=False))


if __name__ == "__main__":
    main()
