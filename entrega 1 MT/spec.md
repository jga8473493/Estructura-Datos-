# Spec — Cola de prioridad de eventos

**Versión:** 1.0 · **Historias que soporta:** HU-06 (Must), HU-08 · **Prioridad:** Must

## Propósito
Contrato de una colección de eventos del juego que entrega siempre primero el más urgente. Esta spec dice **qué** hace, no **cómo**.

## Conceptos
- **Evento:** elemento con un identificador, un tipo (aparición, disparo, impacto, recolección, muerte) y una **prioridad** entera (mayor número = más urgente).
- **Orden de llegada:** a igual prioridad, sale primero el evento que se insertó antes.

## Operaciones públicas
| Operación | Entrada | Salida | Comportamiento |
|---|---|---|---|
| `insertar` | evento, prioridad | nada | Agrega el evento a la cola |
| `extraer` | — | evento | Quita y devuelve el más urgente; si la cola está vacía, señala error de cola vacía |
| `ver_primero` | — | evento | Devuelve el más urgente sin quitarlo; si está vacía, señala error de cola vacía |
| `esta_vacia` | — | booleano | Indica si no hay eventos |
| `tamano` | — | entero | Cantidad de eventos almacenados |

## Criterios de aceptación
- **CA-12** Los eventos salen por prioridad (mayor primero) y, a igual prioridad, por orden de llegada.
- **CA-13** Los eventos de un tick se muestran en el orden en que se extrajeron.
- **CA-22** Extraer o ver el primero en una cola vacía señala error de cola vacía y no altera la cola.
- **CA-23** Con un solo elemento, `extraer` lo devuelve y la cola queda vacía.
- **CA-24** `tamano` aumenta en 1 con cada `insertar` y disminuye en 1 con cada `extraer`.
- **CA-25** `ver_primero` no modifica el tamaño ni el orden de la cola.

## Casos extremos
Cola vacía · un elemento · prioridades repetidas · prioridad negativa o cero · insertar después de vaciar la cola.

## Fuera de alcance
Cancelar o modificar la prioridad de un evento ya insertado.

## Historial de cambios
- v1.0: versión inicial.
