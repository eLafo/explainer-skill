# Explanation-scope and delivery-conflict evaluation

## Changes reviewed

- Narrowed automatic activation to explanatory content, including explanations of code, while excluding implementation changes.
- Required an explicit incompatibility notice for `chat` plus `--file`, followed by a chat explanation without file output.
- Expanded quality coverage from 21 to 24 cases and activation coverage from 4 to 16 queries.
- Added a repository-level runner with deterministic checks, semantic grading, transcripts, and offline tests.

All instructions remain in English. Spanish output is tested both through `--language es` and a natural-language request. No skill paths, credentials, transcripts, or generated task artifacts are included in this report.

## Method

Both versions ran with `openai-codex/gpt-6.1-sol`, using the same candidate test suite. The baseline was a snapshot of the skill from commit `d569268`; the candidate included the changes above. Each run started in a fresh session and working directory, with only the selected skill advertised. Extensions, automatic skill discovery, and project instructions were disabled.

Quality cases were run once per version in the final comparison. Activation queries were run three times per version, passing by majority. The eight train queries and eight held-out validation queries contain equal positive/negative counts. Validation results were not used to tune the description.

File existence, Markdown delivery, exact block/file equality, and required HTML elements were checked by Python. Semantic assertions were graded by a separate model session and reviewed against the visible outputs. This is not a browser-rendering or accessibility evaluation.

## Results

- **Candidate quality:** 24/24 cases passed.
- **Baseline quality:** 22/24 cases passed; cases 14 and 24 omitted the explicit incompatibility notice.
- **Candidate activation:** 16/16 queries passed by majority; 47/48 individual executions matched expectations. The letter-rewriting query activated in 2/3 runs.
- **Baseline activation:** 16/16 queries passed by majority; 48/48 individual executions matched expectations.
- **Train activation:** 8/8 queries passed for each version.
- **Held-out activation:** 8/8 queries passed for each version.
- **Execution/grading errors:** none in the reported runs.
- **Offline runner tests:** 9/9 passed.

The revised skill improved delivery-conflict handling in this quality comparison, with no observed case-level regressions. Activation did **not** improve over the baseline under this model and isolated configuration. The narrower scope is now explicit and passed the boundary tests, but its benefit cannot be inferred from these activation results.

## Evaluation-harness correction

An initial comparison incorrectly failed candidate case 14 because the runner retained only the final answer. The agent had emitted the required notice in an earlier visible message. The runner now retains all visible assistant messages, and a regression test covers that behavior. The final quality comparison was rerun after the correction; the reported quality figures use that rerun, not the faulty initial verdict.

## Limits and follow-up

These are local observations, not stable reliability estimates. The earlier failures used `gpt-5.6-terra`, while this comparison uses `gpt-6.1-sol`; cross-model results must not be attributed solely to the changes. Automatic activation was tested with the selected skill alone, not alongside competing installed skills.

Before making broader reliability claims, repeat quality cases, test activation under the normal installed-skill configuration, and compare on additional models. Review new failures without tuning against the held-out queries. Raw evidence is local and untracked; use `scripts/README.md` to reproduce the comparison.
