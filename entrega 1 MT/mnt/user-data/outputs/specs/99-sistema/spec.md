# Spec del sistema — Juego tipo Metal Slug (versión inicial)

**Versión:** 0.1 (Entrega 1)

## Qué hace el sistema
Es el núcleo lógico de un juego 2D de desplazamiento lateral jugado en consola. Un soldado recorre un nivel, dispara y recoge armas, esquiva y derrota enemigos que lo persiguen y alcanza la meta. El mundo avanza por ticks, sin turnos.

## Funcionalidades
F-01 Iniciar partida · F-02 Mover al soldado · F-03 Inventario · F-04 Deshacer/rehacer · F-05 Enemigos con ruta · F-06 Eventos en orden · F-07 Victoria/derrota · F-08 Puntajes y búsqueda.

## Componentes previstos
| # | Componente | Estructura | Historias | Estado |
|---|---|---|---|---|
| 01 | Cola de prioridad de eventos | Montículo binario | HU-06 | Especificado en Entrega 1 |
| 02 | Inventario | Lista enlazada simple | HU-03 | Pendiente |
| 03 | Historial de acciones | Dos pilas | HU-04 | Pendiente |
| 04 | Entidades activas | Lista doble | HU-08 | Pendiente |
| 05 | Mapa del nivel | Matriz dispersa | HU-01, HU-02 | Pendiente |
| 06 | Ruta de enemigos | Grafo + BFS | HU-05 | Pendiente |
| 07 | Ranking y búsqueda | Árbol AVL | HU-09 | Pendiente |

## Cómo encajan los contratos
En cada tick: (1) se leen la acción del jugador y las decisiones de los enemigos; (2) se **insertan** eventos en el componente 01; (3) se **extraen** y procesan por prioridad; (4) los eventos modifican inventario (02), entidades (04) y mapa (05); (5) las acciones de inventario se registran en el historial (03); (6) los enemigos calculan su ruta con (06) sobre el mapa (05); (7) al terminar la partida, el puntaje entra al ranking (07).

## Reglas globales
- Mayor prioridad = más urgente. Orden de llegada como desempate.
- Todo error de estructura vacía se señala con un error propio, nunca con un fallo silencioso.
- La consola permite ejercitar todas las funcionalidades.

## Fuera de alcance
Gráficos, sonido, multijugador y editor de niveles (ver `moscow.md`).

## Historial de cambios
- v0.1: versión inicial.
