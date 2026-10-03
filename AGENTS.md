# Agent instructions

The installable skill lives in `skills/explainer/`. Keep all referenced paths relative to that skill directory. Repository documentation, license, and release automation belong at the repository root.

Use Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`) for changes intended for the default branch so release-please can determine the next version. A release pull request, not an ordinary push, creates the tag and GitHub Release after it is merged.

Do not commit credentials, private data, local output artifacts, or personal paths. Never claim that following a profile certifies compliance with an external standard.
