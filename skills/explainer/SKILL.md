---
name: explainer
description: "Genera o reformula explicaciones en cualquier idioma. Aplica un perfil de explicación (ASD-STE100, Feynman o lenguaje claro inspirado en ISO 24495-1) y un framework narrativo independientes; entrega en chat, Markdown copiable o HTML. Usa cuando se pida explicar, simplificar o presentar contenido en uno de estos destinos."
license: MIT
metadata:
  author: eLafo
  version: "0.2.0" # x-release-please-version
---

# Explainer

Organiza una explicación sin confundir cuatro decisiones: **qué se sabe** (fuente o tema), **cómo se explica y redacta** (perfil), **en qué orden se entiende** (framework narrativo) y **cómo se entrega** (destino). La forma del documento (artículo, FAQ, procedimiento) es opcional y distinta del framework. El perfil se aplica al texto, sin alterar los hechos. Admite cualquier idioma.

## Interfaz

`/skill:explainer [--profile <id>] [--framework <id>] [--form auto|article|faq|procedure] [--target chat|markdown|html] [--language <idioma>] [--audience <audiencia>] [--file <ruta>] [--strict] [--keep-structure] <petición o contenido>`

Los argumentos son convenciones que interpreta el agente, **no** flags de un parser ejecutable. También se aceptan peticiones equivalentes en lenguaje natural.

- `--profile <id>`: reglas lingüísticas o pedagógicas; por defecto `asd-ste100` **solo si no se pide otro perfil**. «Lenguaje claro», «lenguaje simple» o «plain language» seleccionan `plain-language`; «como Feynman» selecciona `feynman`. «Lectura fácil» validada es una petición distinta: no la equipares automáticamente a lenguaje claro. Consulta `references/profiles/README.md` y **lee siempre** `references/profiles/<id>.md` antes de redactar, también para respuestas cortas.
- `--framework <id>`: recorrido narrativo; por defecto `auto` (no fuerza un relato). Consulta `references/frameworks/README.md` y lee la referencia completa del framework elegido.
- `--form`: forma del documento; `auto` (predeterminado) deja que el contenido determine el formato de organización, `article` usa secciones, `faq` usa preguntas y respuestas, `procedure` organiza **solo acciones presentes en la fuente** en pasos ordenados. La forma no aporta hechos nuevos.
- `--target`: `chat` (predeterminado), `markdown` (bloque copiable, con archivo opcional) o `html` (archivo completo). Lee `references/targets.md` para la entrega y su verificación.
- `--language`: idioma de salida explícito. Prioridad: flag `--language` → petición en lenguaje natural («en inglés», «escríbelo en francés») → idioma de la petición. **No** uses por defecto el idioma del texto fuente si el usuario pide otro. Traduce cuando sea necesario y conserva cifras, condiciones y advertencias. Pregunta solo si la petición multilingüe no expresa preferencia clara.
- `--audience`: adapta términos y detalle al público sin inventar datos.
- `--file <ruta>`: para `markdown`, guarda además el mismo contenido en un `.md`; para `html`, indica la ruta del archivo. No se aplica a `chat`. No sobrescribas un archivo existente sin permiso.
- `--strict`: revisa con más rigor las reglas disponibles; nunca equivale a una certificación o verificación oficial.
- `--keep-structure`: al reformular, conserva títulos, listas, tablas y orden cuando sea posible. Si contradice un framework o una forma explícitos, pide elegir cuál tiene prioridad.

**Compatibilidad:** `--format asd-ste100` equivale a `--profile asd-ste100`; `--structure article|faq|procedure|auto` equivale a `--form` con el mismo valor. Para elegir el recorrido usa `--framework`, y para HTML o Markdown usa `--target`. Si `--format` o `--structure` recibe otro valor, explica el cambio y pide aclaración. Si falta un valor requerido o el ID no está registrado, ofrece las opciones válidas y pregunta; no inventes perfiles ni frameworks.

## Ejemplos

- `--profile asd-ste100 --framework why-how-what --target chat --language es explica ASD-STE100` → respuesta en el chat con redacción clara en español.
- `--profile feynman --target chat explica este concepto a principiantes` → explicación pedagógica sin perder precisión.
- `--profile plain-language --target chat --language es aclara esta carta para sus destinatarios` → lenguaje claro sin omitir condiciones.
- `--framework pyramid --target markdown --file ./resumen.md explica este informe` → bloque Markdown copiable y el mismo contenido en un archivo.
- `--framework scqa --target html explica este problema` → archivo HTML autónomo, siempre que el problema esté documentado.

## Flujo

1. Determina si el usuario pide generar un documento sobre un tema o reformular texto. Si dice «lo anterior», usa la respuesta relevante más reciente. Resuelve **primero el idioma de salida**, incluido lo pedido en lenguaje natural, y después audiencia, perfil, framework, forma y destino. Si falta información imprescindible, pregunta o delimita el alcance; no inventes especificaciones.
2. Antes de escribir, lee íntegramente la referencia del perfil elegido **aunque no se haya indicado `--profile`**. Si se elige un framework distinto de `auto`, lee su referencia. Para `markdown` o `html`, lee `references/targets.md`. Si vas a afirmar datos de un estándar o atribuir un método, consulta la ficha pertinente en `references/sources/README.md` y sus fuentes primarias; no inventes una fuente oficial cuando no existe ficha verificada. Para `asd-ste100`, distingue inglés técnico de adaptación a otro idioma: no cambies el idioma solicitado para ajustarlo al estándar.
3. Extrae las afirmaciones, cifras, condiciones, advertencias e incertidumbres de la fuente. Aplica el framework **solo a contenido sustentado**. No inventes porqués, problemas, pruebas, causas, recomendaciones ni pasos para rellenar casillas. Si falta una pieza necesaria, omítela con honestidad o pregunta cuando impida responder.
4. Aplica la forma y el destino. Mantén el orden obligatorio de acciones y avisos de seguridad: ni un framework narrativo ni una forma editorial deben reordenar un procedimiento peligroso. Si la combinación solicitada es incompatible, explica el conflicto y pide elegir.
5. Comprueba que **el texto final está en el idioma solicitado** (no en el idioma original si difieren). Si hubo traducción, coteja cifras, condiciones, negaciones y advertencias con la fuente. Revisa fidelidad, claridad, límites del perfil, forma y entrega real. Entrega el texto o una ruta al archivo; anota únicamente las limitaciones relevantes (por ejemplo, no atribuyas conformidad oficial a una adaptación).

## Límites

- Ningún perfil acredita conformidad oficial sin verificar todas las reglas y vocabulario del estándar correspondiente.
- Conserva ambigüedades de la fuente o pide aclaración cuando sea imprescindible; no adivines.
- Conserva nombres propios, identificadores, código, comandos, unidades y citas exactas cuando cambiarlos altere el significado.
- Prioriza la exactitud sobre la simplicidad o la fuerza narrativa.
