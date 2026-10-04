---
name: explainer
description: "Use when asked to explain concepts or code, simplify explanatory prose, or rewrite documents for an audience in any language. Apply an independent explanation profile (ASD-STE100, Feynman, or plain language inspired by ISO 24495-1) and narrative framework; deliver in chat, copyable Markdown, or HTML. Explaining code is in scope; writing, modifying, refactoring, debugging, or optimizing executable code is not. Do not activate for code changes merely because the request says simplify."
license: MIT
metadata:
  author: eLafo
  version: "0.3.0" # x-release-please-version
---

# Explainer

Organize an explanation without confusing four decisions: **what is known** (source or topic), **how it is explained and written** (profile), **the order in which it is understood** (narrative framework), and **how it is delivered** (target). The document form (article, FAQ, or procedure) is optional and separate from the framework. Apply the profile to the text without changing the facts. The skill supports any language.

## Scope

Explain concepts, documents, and code without changing executable behavior. Requests to write, modify, refactor, debug, or optimize code belong to coding workflows, not this skill. A request to explain code remains in scope; a request to simplify its implementation does not. For mixed requests, apply this skill only to the explanatory portion.

## Interface

`/skill:explainer [--profile <id>] [--framework <id>] [--form auto|article|faq|procedure] [--target chat|markdown|html] [--language <language>] [--audience <audience>] [--file <path>] [--strict] [--keep-structure] <request or content>`

The arguments are conventions interpreted by the agent, **not** flags handled by an executable parser. Equivalent natural-language requests are also accepted.

- `--profile <id>`: linguistic or teaching rules; defaults to `plain-language` **unless another profile is requested**. “Plain language,” “clear language,” or “simple language” select `plain-language`; “like Feynman” selects `feynman`; “following ASD-STE100” or an equivalent instruction selects `asd-ste100`. Mentioning ASD-STE100 as the **topic** is not enough to select that profile. Validated “easy read” is a different request; do not automatically equate it with plain language. Consult `references/profiles/README.md` and **always read** `references/profiles/<id>.md` before writing, including for short answers.
- `--framework <id>`: narrative path; defaults to `auto`, which does not force a narrative. Consult `references/frameworks/README.md` and read the complete reference for the selected framework.
- `--form`: document form. `auto` (default) lets the content determine its organization; `article` uses sections; `faq` uses questions and answers; `procedure` organizes **only actions present in the source** as ordered steps. Form does not add new facts.
- `--target`: `chat` (default), `markdown` (a copyable block with an optional file), or `html` (a complete file). Read `references/targets.md` for delivery and verification requirements.
- `--language`: explicit output language. Priority: `--language` flag → natural-language request (“in English,” “write it in French”) → language of the request. **Do not** default to the source text’s language when the user requests another one. Translate when necessary and preserve figures, conditions, and warnings. Ask only when a multilingual request gives no clear preference.
- `--audience`: adapt terms and detail to the audience without inventing information.
- `--file <path>`: for `markdown`, also save the same content in a `.md` file; for `html`, specify the output path. It is invalid with `chat`: explicitly explain the incompatibility, create no files, and still deliver the explanation in chat. Do not silently ignore the flag or switch targets. Do not overwrite an existing file without permission.
- `--strict`: review the available rules more rigorously; it never means certification or official verification.
- `--keep-structure`: when rewriting, preserve headings, lists, tables, and order where possible. If it conflicts with an explicit framework or form, ask which takes priority.

**Compatibility:** `--format asd-ste100` is equivalent to `--profile asd-ste100`; `--structure article|faq|procedure|auto` is equivalent to `--form` with the same value. Use `--framework` to select the narrative path and `--target` for HTML or Markdown. If `--format` or `--structure` receives another value, explain the change and ask for clarification. If a required value is missing or an ID is not registered, offer the valid options and ask; do not invent profiles or frameworks.

## Examples

- `--profile asd-ste100 --framework why-how-what --target chat --language es explain ASD-STE100` → a clearly written response in Spanish, delivered in chat.
- `--profile feynman --target chat explain this concept to beginners` → a teaching-oriented explanation that remains accurate.
- `--target chat --language es clarify this letter for its recipients` → plain language by default, without omitting conditions.
- `--framework pyramid --target markdown --file ./summary.md explain this report` → a copyable Markdown block and identical content in a file.
- `--framework scqa --target html explain this problem` → a self-contained HTML file, provided that the problem is documented.

## Workflow

1. Determine whether the user wants a new document about a topic or a rewrite of existing text. If the user says “the previous one,” use the most recent relevant response. Resolve **the output language first**, including natural-language requests, then the audience, profile, framework, form, and target. If essential information is missing, ask or limit the scope; do not invent specifications.
2. Before drafting, check delivery arguments. If `chat` and `--file` are combined, explicitly tell the user that chat does not support file output, then continue in chat without creating a file. This specific conflict does not require clarification; other incompatible combinations still do. Before writing, read the selected profile reference in full **even when `--profile` was not specified**. If a framework other than `auto` is selected, read its reference. For `markdown` or `html`, read `references/targets.md`. Before stating facts about a standard or attributing a method, consult the relevant entry in `references/sources/README.md` and its primary sources; do not invent an official source when no verified entry exists. For `asd-ste100`, distinguish technical English from an adaptation to another language: do not change the requested language to fit the standard.
3. Extract claims, figures, conditions, warnings, and uncertainties from the source. Apply the framework **only to supported content**. Do not invent reasons, problems, evidence, causes, recommendations, or steps to fill template slots. If a necessary element is missing, omit it honestly or ask when its absence prevents an answer.
4. Apply the form and target. Preserve the required order of actions and safety warnings: neither a narrative framework nor an editorial form may reorder a hazardous procedure. If the requested combination is incompatible, explain the conflict and ask the user to choose.
5. Verify that **the final text is in the requested language**, not the source language when they differ. After translation, compare figures, conditions, negations, and warnings with the source. Review fidelity, clarity, profile limits, form, and actual delivery. Deliver the text or a file path; mention only relevant limitations, such as not attributing official conformity to an adaptation.

## Limits

- No profile establishes official conformity unless all rules and vocabulary of the applicable standard have been verified.
- Preserve ambiguities in the source or ask for clarification when necessary; do not guess.
- Preserve proper names, identifiers, code, commands, units, and exact quotations when changing them would alter the meaning.
- Prioritize accuracy over simplicity or narrative force.
