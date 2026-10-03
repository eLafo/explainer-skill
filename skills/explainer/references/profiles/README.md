# Registro de perfiles de explicación

Un perfil determina **cómo se explica y redacta el contenido**, no el framework narrativo, la forma del documento ni el tipo de archivo. Algunos perfiles también piden comprobar si la información es fácil de encontrar y usar en el destino elegido. El identificador se usa con `--profile`. Cada perfil tiene `references/profiles/<id>.md` con reglas operativas, límites y comprobación.

- `asd-ste100` — pautas de claridad técnica basadas en ASD-STE100 para inglés; adaptación inspirada en ellas para otros idiomas. Disponible. No verifica conformidad con el estándar oficial.
- `feynman` — explicación pedagógica con palabras propias, términos definidos y ejemplos concretos cuando ayuden. Disponible. No es un estándar formal.
- `plain-language` — lenguaje claro multilingüe, inspirado en los principios públicos de ISO 24495-1:2023. Disponible y predeterminado cuando no se solicita otro perfil. No verifica conformidad con la norma.

Para añadir un perfil: crea su referencia, registra aquí el ID y actualiza `SKILL.md` si cambia la interfaz. No reutilices un ID de perfil como nombre de destino. El alias antiguo `--format asd-ste100` se mantiene solo por compatibilidad.
