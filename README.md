# Explainer

`explainer` is a skill that generates or rewrites explanations in any language. Use it to clarify text, explain a topic, or adapt content to an audience.

The skill separates four decisions:

- **Profile:** defines how the content is explained and written.
- **Narrative framework:** defines the order of ideas.
- **Form:** organizes the document as an article, FAQ, or procedure.
- **Target:** delivers the result in chat, as copyable Markdown, or as an HTML file.

## Install the skill

Run:

```bash
npx skills add elafo/explainer-skill --skill explainer
```

Installation applies to the current project. Add `-g` to install the skill globally.

Review its contents before installation. Installing from GitHub does not automatically pin a published version.

## Choose a profile

If you do not choose a profile, the skill uses `plain-language`.

- `plain-language`: multilingual plain language inspired by the public principles of ISO 24495-1:2023.
- `feynman`: a teaching-oriented explanation inspired by Feynman.
- `asd-ste100`: partial guidelines for writing clear technical English.

These profiles guide the writing. **They do not establish conformity with an official standard.** See the sources and limits for each attribution in [`skills/explainer/references/sources/`](skills/explainer/references/sources/).

## Choose the language and target

Specify the language with `--language` or request it in natural language.

The skill can deliver the result as:

- a chat response;
- a copyable Markdown block;
- an HTML file.

For Markdown, `--file` also saves the content to a file. For HTML, `--file` specifies the path of the file to create.

## Main files

The installable skill is in [`skills/explainer/`](skills/explainer/).

- [`skills/explainer/SKILL.md`](skills/explainer/SKILL.md) contains the main instructions.
- [`skills/explainer/references/`](skills/explainer/references/) contains additional rules.
- [`skills/explainer/references/sources/`](skills/explainer/references/sources/) records verified primary sources and their limits.
- [`skills/explainer/evals/evals.json`](skills/explainer/evals/evals.json) contains evaluation cases, expected results, and assertions.
- [`skills/explainer/evals/trigger-queries.json`](skills/explainer/evals/trigger-queries.json) contains cases for evaluating skill activation.

The evaluation cases are proposals. The complete suite has not yet been run to measure reliability.

## Releases

This repository uses [release-please](https://github.com/googleapis/release-please-action) and Conventional Commits to propose new versions.

A new version is published when a release pull request is merged. The tag and GitHub Release are created at that time. An ordinary push does not publish a version.

The first version was `v0.1.0`. See the [published releases](https://github.com/eLafo/explainer-skill/releases) for the current version.
