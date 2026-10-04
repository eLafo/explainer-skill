# Explainer

`explainer` es una skill que genera o reescribe explicaciones en cualquier idioma. Puedes usarla para aclarar un texto, explicar un tema o adaptar el contenido a una audiencia.

La skill separa cuatro decisiones:

- **Perfil:** define cómo se explica y se redacta el contenido.
- **Framework narrativo:** define el orden de las ideas.
- **Forma:** organiza el documento como artículo, preguntas frecuentes o procedimiento.
- **Destino:** entrega el resultado en el chat, como Markdown copiable o como archivo HTML.

## Instalar la skill

Ejecuta:

```bash
npx skills add elafo/explainer-skill --skill explainer
```

La instalación se aplica al proyecto actual. Añade `-g` si quieres instalar la skill de forma global.

Revisa su contenido antes de instalarla. La instalación desde GitHub no fija de forma automática una versión publicada.

## Elegir un perfil

Si no eliges un perfil, la skill usa `plain-language`.

- `plain-language`: lenguaje claro multilingüe inspirado en los principios públicos de ISO 24495-1:2023.
- `feynman`: explicación pedagógica inspirada en Feynman.
- `asd-ste100`: pautas parciales para redactar inglés técnico claro.

Estos perfiles orientan la redacción. **No acreditan conformidad con una norma oficial.** Puedes consultar las fuentes y los límites de cada atribución en [`skills/explainer/references/sources/`](skills/explainer/references/sources/).

## Elegir el idioma y el destino

Puedes indicar el idioma con `--language` o pedirlo en lenguaje natural.

La skill puede entregar el resultado en:

- el chat;
- un bloque Markdown copiable;
- un archivo HTML.

Cuando eliges Markdown, `--file` guarda también el contenido en un archivo. Cuando eliges HTML, `--file` indica la ruta del archivo que se debe crear.

## Archivos principales

La skill instalable está en [`skills/explainer/`](skills/explainer/).

- [`skills/explainer/SKILL.md`](skills/explainer/SKILL.md) contiene las instrucciones principales.
- [`skills/explainer/references/`](skills/explainer/references/) contiene las reglas adicionales.
- [`skills/explainer/references/sources/`](skills/explainer/references/sources/) registra las fuentes primarias verificadas y sus límites.
- [`skills/explainer/evals/evals.json`](skills/explainer/evals/evals.json) contiene casos de evaluación, resultados y aserciones.
- [`skills/explainer/evals/trigger-queries.json`](skills/explainer/evals/trigger-queries.json) contiene casos para evaluar la activación de la skill.

Los casos de evaluación son propuestas. La batería completa todavía no se ha ejecutado para medir la fiabilidad.

## Versiones

Este repositorio usa [release-please](https://github.com/googleapis/release-please-action) y commits convencionales para proponer nuevas versiones.

Una nueva versión se publica cuando se fusiona una pull request de release. En ese momento se crean la etiqueta y la GitHub Release. Un push normal no publica una versión.

La primera versión fue `v0.1.0`. Consulta las [versiones publicadas](https://github.com/eLafo/explainer-skill/releases) para conocer la versión actual.
