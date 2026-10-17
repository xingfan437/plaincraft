# PlainCraft response trial — 2026-10-17

This is a small **development smoke test**, not a benchmark showing that PlainCraft makes a model smarter or more Claude-like. The result was a near tie: the baseline was already direct and context-aware, and all three code samples were effectively identical between conditions.

## Method

Two fresh Codex subagents used the parent's inherited model and settings, with no model override. One received only the [six synthetic scenarios](scenarios.json); the other also read PlainCraft's updated `SKILL.md`. Neither received expected answers, a scoring rubric, the other's responses or the author's conclusions. Tasks were response-only: no deployment, real file access, external services or GPU work. Each agent handled all six prompts and wrote one sample per prompt, treating prompts independently. They did not have isolated fresh sessions for each individual scenario.

Host system/developer instructions were still active in both agents, so this is an **incremental test in this Codex environment**, not an unprompted base-model comparison. The baseline may already receive similar communication guidance. The harness did not expose or pin a separate model snapshot, seed or sampling parameters. No Claude model was called. The author reviewed the outputs unblinded; no external human preference ratings were collected.

Raw outputs: [baseline](results/baseline.json), [PlainCraft](results/plaincraft.json). They are retained as generated, including host-specific writing-block markup. Style illustrations elsewhere are separate authored material.

## Observations

| Scenario | Baseline | With PlainCraft |
| --- | --- | --- |
| Follow-up about offline Windows invoice copies | Requests path and examples; keeps originals and offline operation | Requests path and examples; explicitly carries forward no-install constraint and new output folder |
| Integer page-count helper | Correct ceiling division; no redundant internal checks | Same algorithm and nearly identical explanation |
| Maximum half-open interval overlap | Correct event sorting; endings before starts | Same algorithm and explanation |
| Short Spanish dinner decline | Brief, polite, no invented excuse | Brief, polite, no invented excuse; host wraps it as a reusable message |
| Timed-out deployment status | Does not claim launch or outage | Does not claim launch or outage; says verification is still needed |
| External JSON integer boundary | Rejects booleans, invalid bounds and missing field | Same validation and nearly identical explanation |

The invoice response makes one constraint more explicit, but the baseline also satisfies the request. That is not enough evidence to establish a reliable improvement. The writer preferred neither condition conclusively. Spanish naturalness has not been rated by independent speakers; other languages were not behavior-tested in this trial.

## Executable code checks

After manual inspection, the author ran the three returned functions from each condition against **28 cases per condition**: seven page-count cases, seven interval cases and fourteen quantity cases. **Baseline: 28/28; PlainCraft: 28/28.** The cases include zero and exact multiples, a large integer, touching endpoints, unsorted intervals, boolean rejection and missing fields.

Reproduce the deterministic checks on the bundled samples:

```console
python evals/check_code.py
```

[Full machine-readable result](results/code-checks.json). The runner executes the reviewed snippets; it is not a sandbox for arbitrary new code. These checks rerun saved answers, rather than regenerate model responses. The individual cases are small; passing them does not establish unchanged coding ability on repositories or difficult tasks.

## What changed after testing

No failing behavior in this trial justified another prompt rule. We kept the language-neutral revision and documented the limited result instead of tuning it to win these six prompts. The skill checksum at evaluation time is recorded in [metadata.json](metadata.json). Subsequent documentation and calibration-example edits are tracked separately from the evaluated entrypoint.

## Next useful evidence

Real-user, consented comparisons across models and languages would be more informative. Randomize answer order, include “tie” as an option, and record factual omissions and code regressions alongside preference. Keep an untouched holdout set when revising instructions. Do not select only flattering examples or publish private transcripts.

中文结论：三道编码题两组各通过 28 个检查，回答差异很小。它是可用的协作指令初版，但尚未证明变聪明、整体编码能力不变或达到 Claude 的体验。
