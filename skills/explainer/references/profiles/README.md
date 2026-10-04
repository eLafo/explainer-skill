# Explanation profile registry

A profile determines **how content is explained and written**, not the narrative framework, document form, or file type. Some profiles also require checking whether information is easy to find and use in the selected target. Use the identifier with `--profile`. Each profile has a `references/profiles/<id>.md` file containing operational rules, limits, and checks.

- `asd-ste100` — technical clarity guidelines based on ASD-STE100 for English, with an inspired adaptation for other languages. Available. Does not verify conformity with the official standard.
- `feynman` — teaching-oriented explanation in the writer’s own words, with defined terms and concrete examples when useful. Available. Not a formal standard.
- `plain-language` — multilingual plain language inspired by the public principles of ISO 24495-1:2023. Available and used by default when no other profile is requested. Does not verify conformity with the standard.

To add a profile, create its reference, register its ID here, and update `SKILL.md` if the interface changes. Do not reuse a profile ID as a target name. The legacy alias `--format asd-ste100` is retained only for compatibility.
