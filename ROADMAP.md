# Explainer roadmap

This document collects pending proposals and decisions that have already been applied. Proposals are not available features. The current interface and supported identifiers are in [`skills/explainer/SKILL.md`](skills/explainer/SKILL.md). Keep profile (how to explain), framework (order of ideas), document form, and target (delivery) separate.

## Next iteration: precision when interpreting LLM output

- [ ] **Profile `precision-first`** — explain clearly without removing conditions, uncertainty, exceptions, or technical distinctions. Do not turn a hypothesis into a fact or summarize by default.
- [ ] **Framework `claim-evidence-limits`** — claim → available evidence → limits and unknown data. If evidence is missing, say so; do not create evidence to complete the sequence.
- [ ] Add evaluations with ambiguous input, incomplete data, and unsupported claims. Compare fidelity and usefulness with existing profiles and frameworks before adopting both additions.

## Later profiles and frameworks

- [ ] **Profile `easy-read`** — writing for specific cognitive accessibility needs. Distinguish it from `plain-language`; consult relevant official sources and validate with the intended audience. Do not claim “validated easy read” merely because guidelines were applied.
- [ ] **Framework `worked-example`** — concept → worked example → general rule → new case. Complements the `feynman` profile by fixing the teaching sequence rather than vocabulary. Mark hypothetical examples as such.
- [ ] **Framework `comparison`** — criteria → differences → trade-offs → choice, only when sufficient options and data exist. Do not invent criteria, advantages, or recommendations.

## New targets, in priority order

- [ ] **`pdf`** — a self-contained, printable document. Define generation, dependencies, and checks for selectable text, pagination, readability, and metadata; do not replace the content with an image.
- [ ] **`json`** — output for other systems, with a schema and validation. The profile affects only explanatory text values, not keys or data types. Define file delivery and handling of unknown data.
- [ ] **`slides-html`** — a self-contained, screen-based HTML presentation. Preserve readability, keyboard navigation, and correspondence between the script and visible content; validate desktop and mobile layouts. It does not require another skill.

## Applied product decision

- [x] **Default profile: `plain-language`.** For general requests without an explicit profile, use plain language in the requested language. `asd-ste100` remains available through `--profile asd-ste100`, the `--format asd-ste100` alias, or an explicit equivalent natural-language request; mentioning it only as the topic does not select it. Retain compatibility and multilingual-response evaluations.

## Criteria for each addition

1. Document scope, limits, and sources in `references/` without promising conformity with standards whose full text or review has not been verified.
2. Keep each axis independent; prevent a framework from requiring invented information or a target from changing the meaning.
3. Add activation and quality cases to `skills/explainer/evals/`; test positive requests, edge cases, and similar requests that should not activate the skill.
4. Update `SKILL.md`, the README, and the relevant registry only when the capability has been implemented and validated. Do not advertise roadmap items as available.
