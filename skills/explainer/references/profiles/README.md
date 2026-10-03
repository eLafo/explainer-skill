# Registro de perfiles lingüísticos

Un perfil determina **cómo se redacta el texto**, no la estructura del documento ni el tipo de archivo. El identificador se usa con `--profile`. Cada perfil tiene `references/profiles/<id>.md` con reglas operativas, límites y comprobación.

- `asd-ste100` — pautas de claridad técnica basadas en ASD-STE100 para inglés; adaptación inspirada en ellas para otros idiomas. Disponible. No verifica conformidad con el estándar oficial.
- `feynman` — explicación pedagógica con palabras propias, términos definidos y ejemplos concretos cuando ayuden. Disponible. No es un estándar formal.

Para añadir un perfil: crea su referencia, registra aquí el ID y actualiza `SKILL.md` si cambia la interfaz. No reutilices un ID de perfil como nombre de destino. El alias antiguo `--format asd-ste100` se mantiene solo por compatibilidad.
