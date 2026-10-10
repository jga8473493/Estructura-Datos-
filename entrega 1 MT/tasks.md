# Tareas — Cola de prioridad de eventos

Regla: una tarea = un commit. Cada prueba lleva en su docstring el criterio que verifica.
Orden: primero las pruebas, luego el código.

| # | Tarea | Cierra | Prueba (`tests/test_cola_prioridad.py`) | Estado |
|---|---|---|---|---|
| T-01 | Crear `ColaVaciaError` y la clase vacía con `esta_vacia` y `tamano` | CA-24 (base) | `test_nueva_cola_esta_vacia` | [ ] |
| T-02 | Escribir pruebas de extremos (vacía, un elemento) | CA-22, CA-23 | `test_extraer_vacia_error`, `test_ver_primero_vacia_error`, `test_un_elemento` | [ ] |
| T-03 | Implementar `insertar` con ascenso en el montículo | CA-24 | `test_tamano_aumenta`, `test_insertar_mantiene_maximo_arriba` | [ ] |
| T-04 | Implementar `extraer` con descenso | CA-12, CA-24 | `test_extraer_por_prioridad`, `test_tamano_disminuye` | [ ] |
| T-05 | Agregar `secuencia` para desempate por llegada | CA-12 | `test_empate_sale_por_llegada` | [ ] |
| T-06 | Implementar `ver_primero` sin modificar | CA-25 | `test_ver_primero_no_modifica` | [ ] |
| T-07 | Integrar al bucle de ticks y mostrar el orden en consola | CA-13 | `test_eventos_del_tick_en_orden_de_extraccion` | [ ] |
| T-08 | Docstrings con complejidad y fila en `ANALISIS.md` | — | revisión manual | [ ] |

Mínimo 3 pruebas por operación pública (se completan en T-02 a T-06).
