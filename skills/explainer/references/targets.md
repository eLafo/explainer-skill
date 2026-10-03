# Destinos de Explainer

Un destino determina cómo **se entrega** la explicación, no qué vocabulario usa ni qué recorrido narrativo sigue. Destinos disponibles: `chat`, `markdown`, `html`. El idioma del texto depende de `--language`. No hagas depender un destino de otra skill.

## `chat` (predeterminado)

Responde directamente en la conversación. Puedes usar títulos o listas cortas si ayudan, pero no envuelvas toda la respuesta en un bloque de código. No crees archivos. `--file` no es válido con este destino.

## `markdown`

Entrega **todo el documento** en un único bloque de código Markdown copiable, con etiqueta `markdown` (o `md` si el cliente solo acepta esa etiqueta). No pongas prólogos, notas o líneas ajenas al documento dentro del bloque. Si el documento contiene fences, usa un delimitador exterior más largo para que pueda copiarse íntegro. El documento puede contener títulos, listas, tablas o citas si sirven al contenido; no impongas secciones vacías.

Si se indica `--file <ruta>`, escribe además **exactamente el mismo documento** en un archivo `.md`. Muestra la ruta fuera del bloque y no sobrescribas un archivo existente sin permiso. Sin `--file`, no crees archivo: el snippet es la entrega.

## `html`

Entrega un **archivo HTML completo**, no solo un fragmento o una descripción. Incluye `<!doctype html>`, `<html lang="…">`, `<meta charset>`, viewport, `<title>` y HTML semántico. Integra el CSS necesario en el archivo; no dependas de redes externas para mostrar la página. Mantén el texto seleccionable, la jerarquía de títulos clara, el contraste suficiente y una presentación que se adapte a pantallas pequeñas. El perfil se aplica a todo el texto visible, incluidas etiquetas y pies.

Usa `--file <ruta>` si se indica; exige extensión `.html`. Si no hay ruta, crea un nombre descriptivo y **nuevo** bajo `./explainer-output/` del directorio de trabajo; añade un sufijo si ya existe. No sobrescribas sin permiso. Comprueba que el archivo existe, es un documento completo y se puede abrir; entrega la ruta.

## Ampliación

Para añadir otro destino, documenta sus requisitos, modo de entrega y verificación aquí antes de anunciarlo en `SKILL.md`. No cambies el significado de `--profile` o `--framework` para codificar una extensión de archivo o un medio audiovisual.
