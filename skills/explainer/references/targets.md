# Explainer targets

A target determines how the explanation **is delivered**, not which vocabulary it uses or which narrative path it follows. Available targets: `chat`, `markdown`, and `html`. The text language depends on `--language`. Do not make a target depend on another skill.

## `chat` (default)

Respond directly in the conversation. Use headings or short lists when helpful, but do not wrap the entire response in a code block. Do not create files. `--file` is not valid with this target. When both are requested, explicitly explain that chat does not support file output, create no files, and deliver the explanation in chat. Do not merely say that no file was created, silently ignore the flag, or change the target. Any wording that clearly communicates the incompatibility is acceptable.

## `markdown`

Deliver **the entire document** in one copyable Markdown code block with the `markdown` language tag, or `md` if the client accepts only that tag. Do not put prefaces, notes, or lines external to the document inside the block. If the document contains fences, use a longer outer delimiter so the complete document can be copied. The document can contain headings, lists, tables, or quotations when useful; do not impose empty sections.

If `--file <path>` is specified, also write **exactly the same document** to a `.md` file. Show the path outside the block, and do not overwrite an existing file without permission. Without `--file`, do not create a file; the snippet is the delivery.

## `html`

Deliver a **complete HTML file**, not only a fragment or description. Include `<!doctype html>`, `<html lang="…">`, `<meta charset>`, a viewport declaration, `<title>`, and semantic HTML. Embed the necessary CSS in the file; do not depend on external networks to display the page. Keep text selectable, maintain a clear heading hierarchy and sufficient contrast, and make the presentation adapt to small screens. Apply the profile to all visible text, including labels and footers.

Use `--file <path>` when provided and require a `.html` extension. If no path is provided, create a descriptive, **new** filename under `./explainer-output/` in the working directory; add a suffix if it already exists. Do not overwrite without permission. Verify that the file exists, is a complete document, and can be opened; deliver its path.

## Extension

Before advertising another target in `SKILL.md`, document its requirements, delivery method, and verification here. Do not change the meaning of `--profile` or `--framework` to encode a file extension or audiovisual medium.
