"""Check code from the bundled, manually inspected response samples.

Not a sandbox or an evaluator for arbitrary model output. Review changed samples
before executing. Run with Python 3.10+; no model calls or third-party packages.
"""

import ast
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent


def load_function(response, name):
    blocks = re.findall(r"```python\s*\n(.*?)```", response, re.S)
    if len(blocks) != 1:
        raise ValueError("Expected one reviewed Python block: " + name)
    tree = ast.parse(blocks[0])
    if len(tree.body) != 1 or not isinstance(tree.body[0], ast.FunctionDef) or tree.body[0].name != name:
        raise ValueError("Expected the named function only: " + name)
    if any(isinstance(node, (ast.Import, ast.ImportFrom)) for node in ast.walk(tree)):
        raise ValueError("Imports require manual review")
    namespace = {"__builtins__": {"dict": dict, "int": int, "ValueError": ValueError, "isinstance": isinstance, "type": type, "sorted": sorted, "max": max}}
    exec(compile(tree, "<reviewed-response>", "exec"), namespace)
    return namespace[name]


def check_responses(path):
    responses = {item["id"]: item["response"] for item in json.loads(path.read_text(encoding="utf-8"))}
    results = []

    def check(label, function, args, expected=None, error=False):
        try:
            actual = function(*args)
            passed = not error and type(actual) is int and actual == expected
            detail = repr(actual)
        except Exception as exc:
            passed = error and type(exc) is ValueError
            detail = type(exc).__name__
        results.append({"case": label, "passed": passed, "actual": detail})

    page_count = load_function(responses["batches"], "page_count")
    for n, size, expected in [(0, 10, 0), (1, 10, 1), (9, 10, 1), (10, 10, 1), (11, 10, 2), (20, 10, 2), (10**30, 3, (10**30 + 2) // 3)]:
        check(f"page_count({n}, {size})", page_count, (n, size), expected)

    max_parallel = load_function(responses["overlaps"], "max_parallel")
    for label, intervals, expected in [
        ("empty", [], 0), ("single", [(1, 2)], 1),
        ("touching", [(1, 2), (2, 3)], 1),
        ("nested", [(1, 4), (2, 5), (3, 6)], 3),
        ("unsorted", [(5, 7), (1, 6)], 2),
        ("simultaneous starts and ends", [(1, 3), (1, 3), (3, 5), (3, 5)], 2),
        ("negative times", [(-5, -1), (-3, 0), (0, 1)], 2),
    ]:
        check("max_parallel: " + label, max_parallel, (intervals,), expected)

    parse_quantity = load_function(responses["boundary"], "parse_quantity")
    for value in [1, 25, 50]:
        check("parse_quantity: " + repr(value), parse_quantity, ({"quantity": value},), value)
    for value in [0, 51, -1, True, False, "2", None, 2.0, [], {}]:
        check("parse_quantity rejects " + repr(value), parse_quantity, ({"quantity": value},), error=True)
    check("parse_quantity rejects missing field", parse_quantity, ({},), error=True)
    return {"file": path.name, "passed": sum(item["passed"] for item in results), "total": len(results), "checks": results}


def main():
    reports = [check_responses(ROOT / "results" / (name + ".json")) for name in ("baseline", "plaincraft")]
    print(json.dumps({"scope": "Bundled reviewed samples only; not overall model capability", "reports": reports}, indent=2))
    return 0 if all(item["passed"] == item["total"] for item in reports) else 1


if __name__ == "__main__":
    raise SystemExit(main())
