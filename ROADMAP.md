# Roadmap de Explainer

Este documento reúne propuestas pendientes y decisiones ya aplicadas. Las propuestas no son funcionalidades disponibles. La interfaz actual y los identificadores admitidos están en [`skills/explainer/SKILL.md`](skills/explainer/SKILL.md). Mantener separados perfil (cómo explicar), framework (orden de las ideas), forma del documento y target (entrega).

## Próxima iteración: precisión al interpretar salidas de LLM

- [ ] **Profile `precision-first`** — explicar con claridad sin borrar condiciones, incertidumbre, excepciones ni distinciones técnicas. No convertir una hipótesis en un hecho ni resumir por defecto.
- [ ] **Framework `claim-evidence-limits`** — afirmación → evidencia disponible → límites y datos desconocidos. Si faltan pruebas, decirlo; no crear pruebas para completar la secuencia.
- [ ] Añadir evals con entradas ambiguas, datos incompletos y afirmaciones sin fuente. Comparar fidelidad y utilidad con los perfiles y frameworks existentes antes de adoptar ambos.

## Perfiles y frameworks posteriores

- [ ] **Profile `easy-read`** — redacción pensada para necesidades específicas de accesibilidad cognitiva. Diferenciarlo de `plain-language`; consultar fuentes oficiales pertinentes y validar con personas destinatarias. No declarar «lectura fácil validada» por aplicar unas pautas.
- [ ] **Framework `worked-example`** — concepto → ejemplo resuelto → regla general → nuevo caso. Complementa el perfil `feynman`: fija la secuencia didáctica, no el vocabulario. Los ejemplos hipotéticos deben identificarse como tales.
- [ ] **Framework `comparison`** — criterios → diferencias → compromisos → elección, solo si hay opciones y datos suficientes. No inventar criterios, ventajas o recomendaciones.

## Nuevos targets, por orden de prioridad

- [ ] **`pdf`** — documento autónomo e imprimible. Definir generación, dependencias y comprobaciones de texto seleccionable, paginación, legibilidad y metadatos; no sustituir el contenido por una imagen.
- [ ] **`json`** — salida para otros sistemas, con esquema y validación. El perfil solo afecta a los valores de texto explicativo, no a claves ni tipos de datos. Definir cómo se entregan los archivos y qué ocurre ante datos desconocidos.
- [ ] **`slides-html`** — presentación HTML autónoma por pantallas. Mantener legibilidad, navegación por teclado y correspondencia entre el guion y el contenido visible; validar escritorio y móvil. No requiere otra skill.

## Decisión de producto aplicada

- [x] **Perfil predeterminado: `plain-language`.** En solicitudes generales sin perfil explícito, usar lenguaje claro en el idioma solicitado. `asd-ste100` continúa disponible mediante `--profile asd-ste100`, el alias `--format asd-ste100` o una petición explícita equivalente en lenguaje natural; mencionarlo solo como tema no lo selecciona. Mantener las evaluaciones de compatibilidad y de respuestas multilingües.

## Criterios para cada incorporación

1. Documentar alcance, límites y fuentes en `references/`, sin prometer conformidad con estándares cuyo texto íntegro o revisión no se haya verificado.
2. Mantener cada eje independiente; evitar que un framework obligue a inventar datos o que un target cambie el significado.
3. Añadir casos de activación y de calidad a `skills/explainer/evals/`; probar peticiones positivas, casos límite y peticiones similares que no deban activar la skill.
4. Actualizar `SKILL.md`, README y registro correspondiente solo cuando la capacidad esté implementada y validada. No anunciar elementos del roadmap como disponibles.
