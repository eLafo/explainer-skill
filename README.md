# Explainer

Repositorio de la skill `explainer` para generar o reformular explicaciones. Separa perfil de explicación, framework narrativo, forma del documento, idioma y destino (chat, Markdown copiable o HTML).

La unidad instalable está en [`skills/explainer/`](skills/explainer/). Su entrada es [`skills/explainer/SKILL.md`](skills/explainer/SKILL.md); sus reglas adicionales están en `skills/explainer/references/`. Las fuentes primarias verificadas y sus límites están registradas en [`skills/explainer/references/sources/`](skills/explainer/references/sources/).

Perfiles disponibles: `asd-ste100` (pautas parciales de claridad técnica), `feynman` (pedagogía inspirada en Feynman) y `plain-language` (lenguaje claro multilingüe inspirado en los principios públicos de ISO 24495-1:2023). **El perfil predeterminado es `plain-language`; `asd-ste100` sigue disponible cuando se solicita expresamente. Ninguno acredita conformidad con una norma oficial.** La fuente y los límites de cada atribución se documentan en [`references/sources/`](skills/explainer/references/sources/). Las evaluaciones están en [`skills/explainer/evals/evals.json`](skills/explainer/evals/evals.json) (resultados y aserciones) y [`skills/explainer/evals/trigger-queries.json`](skills/explainer/evals/trigger-queries.json) (activación). Son casos propuestos; la batería completa aún debe ejecutarse para medir fiabilidad.

El idioma de salida se elige con `--language` o en lenguaje natural. Para Markdown, `--file` guarda además el snippet en un archivo; para HTML indica el archivo de entrega.

## Instalación

```bash
npx skills add elafo/explainer-skill --skill explainer
```

La instalación es local al proyecto; añade `-g` para instalarla de forma global. Revisa el contenido de la skill antes de instalarla. La instalación desde GitHub no fija automáticamente una versión de release.

## Versiones

Este repositorio usa [release-please](https://github.com/googleapis/release-please-action) y commits convencionales para proponer versiones. **Al fusionar una PR de release** se crean la etiqueta y la GitHub Release; un push ordinario no publica una versión. La primera release fue `v0.1.0`; consulta las [releases publicadas](https://github.com/eLafo/explainer-skill/releases) para ver la versión vigente.
