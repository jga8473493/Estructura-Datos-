# Plan — Cola de prioridad de eventos

**Versión:** 1.0 · **Spec asociada:** `spec.md` v1.0

## Estructura elegida
**Montículo binario máximo**, guardado en un arreglo interno. Cada nodo guarda `(prioridad, secuencia, evento)`.

## Por qué esta estructura
La operación que más se repite es **insertar y extraer el más urgente** en cada tick. El montículo lo resuelve en O(log n); no se necesita orden total, solo el máximo.

## Orden de llegada (CA-12)
Un montículo no es estable. Se agrega un contador `secuencia` que crece con cada inserción. La comparación es: mayor prioridad primero; si empatan, menor secuencia primero.

## Complejidad
| Operación | Complejidad |
|---|---|
| `insertar` | O(log n) |
| `extraer` | O(log n) |
| `ver_primero` | O(1) |
| `esta_vacia` | O(1) |
| `tamano` | O(1) |

## Alternativas descartadas
- **Cola simple (FIFO):** insertar y extraer son O(1), pero no distingue urgencia; una muerte esperaría detrás de una aparición.
- **Lista ordenada:** extraer es O(1) pero insertar es O(n).
- **Árbol AVL:** O(log n) en todo, pero con más código y rotaciones sin necesitar búsqueda arbitraria.

## Soporte interno
Se usa `list` de Python solo como almacenamiento del arreglo del montículo (permitido por el enunciado). Toda la lógica (subir, bajar, comparar) es propia. No se usa `heapq`.

## Dónde se usa
Bucle de ticks del dominio: los sistemas de combate y de aparición insertan eventos; el bucle los extrae y los procesa.

## Módulo y errores
`estructuras/cola_prioridad.py` · error propio `ColaVaciaError`.

## Historial de cambios
- v1.0: versión inicial.
