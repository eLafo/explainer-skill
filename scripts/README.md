# Evaluation runner

These are repository development tools, not part of the installable skill.

## Requirements

- Python 3.10 or newer (standard library only).
- A current `pi` CLI supporting the flags used by `run-evals.py`.
- Authentication for the explicit provider/model passed with `--model`.

The runner launches real model requests, including a semantic judge, so runs consume model quota. A full comparison currently uses 24 quality runs and 48 activation runs per version, plus semantic grading. No automatic retries are performed.

## Run

Snapshot the old skill before editing it. Its directory must retain the name `explainer`:

```bash
mkdir -p /tmp/explainer-baseline
cp -R skills/explainer /tmp/explainer-baseline/explainer
```

After editing, compare both versions using the same model:

```bash
python3 scripts/run-evals.py \
  --model openai-codex/gpt-6.1-sol \
  --baseline /tmp/explainer-baseline/explainer \
  --output ./eval-results/iteration-1
```

The output directory must not already exist and must be outside the installable skill. Omit `--output` to create a temporary workspace. Omit `--baseline` for a candidate-only run. `--only quality` or `--only trigger` narrows the run. Activation cases default to three executions; change this with `--trigger-runs`. Concurrency defaults to four workers; adjust with `--workers`.

Each version is copied to the workspace before execution. Sessions have no prior context, automatically discovered skills, project instructions, or extensions; only the selected snapshot is advertised. This isolates version comparisons but does not measure competition with other installed skills. Runs are separate working directories, **not OS sandboxes**: Pi can still access files and the network. Run only trusted skills and prompts. Temporary downloads outside the working directory are not included in the generated-task-file inventory.

## Evidence and grading

- `events.jsonl` records full model events and tool calls.
- `outputs/` contains generated task files; logs live outside it.
- `result.json` records verdicts, evidence, model identity, time, and tokens.
- `benchmark.json` summarizes both configurations and trigger rates.
- `results.json` contains all case results.

Mechanical checks use Python for file existence, required HTML elements, Markdown fences, and exact block/file equality. HTML checks are structural, not browser rendering or accessibility certification. Remaining assertions are graded by a fresh model session with concrete evidence; review semantic judgments manually. All visible assistant text, including notices before the final answer, is retained.

Activation means the agent called `read` on the selected `SKILL.md`. Each query passes by majority across three executions. Errors fail the case; they are not counted as successful non-activation. Train and validation labels are fixed in `trigger-queries.json`; use train failures for tuning and keep validation cases out of the tuning loop. Validation rates must be reported separately. Both versions use the candidate's test suite for a fair comparison.

The runner exits nonzero when the candidate has failed cases or execution/grading errors. Baseline failures do not determine its exit code. Single quality executions are observations, not reliability estimates; repeat runs for important regressions. No baseline means no claim of improvement over another version.

Artifacts may contain prompts, personal paths, and provider metadata. Do not commit or publish them. `eval-results/` is ignored by Git.

## Offline checks

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
```
