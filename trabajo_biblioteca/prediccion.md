# Predicción de complejidad

Antes de hacer las mediciones con `timeit`, voy a predecir cuánto debería tardar cada operación dependiendo de la cantidad de elementos que tenga la lista.
Voy a usar `n` para representar la cantidad de elementos.

## obtener(pos)
**O(1)**
Esta operación debería ser muy rápida porque solamente tiene que ir directamente a la posición que se le pide.
Por ejemplo, si quiero el elemento de la posición 500, no se tiene que revisar los anteriores. Va directamente a esa posición.
Por eso es **O(1)**.
---
## insertar(pos, x)
**O(n)**
Cuando metemos un elemento en una posición que no sea el final, tenemos que mover los elementos que están después para dejar espacio.
Por ejemplo:
```text
10 20 30 40
```
Si queremos meter un elemento entre `10` y `20`, tenemos que mover los demás elementos.

Mientras más elementos tenga la lista, más elementos puede tener que mover.

En el peor caso, si insertamos al principio, tendría que mover prácticamente toda la lista.

Por eso es **O(n)**.

---

## insertar_ordenado(x)

**O(n)**

Esta operación tiene que mantener la lista ordenada.

Para hacerlo, empieza desde el final y va revisando los elementos. Si encuentra uno mayor que el nuevo elemento, lo mueve una posición.

Por ejemplo, si tenemos:

```text
10 20 30 40
```

y queremos insertar `5`, tendría que mover todos los elementos para dejar el `5` al principio.

Por eso, en el peor caso, puede recorrer y mover todos los elementos.

Entonces es **O(n)**.

---

## buscar_lineal(x)

**O(n)**

Esta búsqueda va revisando los elementos uno por uno:

```text
elemento 1
elemento 2
elemento 3
...
```

Si el elemento que buscamos está al final, o si directamente no existe, tenemos que revisar toda la lista.

Por ejemplo, con 10.000 elementos podríamos tener que revisar los 10.000.

Por eso es **O(n)**.

---

## buscar_binaria(x)

**O(log n)**

Esta búsqueda necesita que los elementos estén ordenados.

En vez de revisar uno por uno, mira el elemento que está en la mitad.

Después de mirar la mitad, puede descartar aproximadamente la mitad de los elementos y volver a hacer lo mismo.

Por ejemplo:

```text
200.000
100.000
50.000
25.000
12.500
...
```

Por eso necesita muchas menos comprobaciones que la búsqueda lineal.

Su complejidad es **O(log n)**.

---

## Resumen

| Operación              | Complejidad |
| ---------------------- | ----------- |
| `obtener(pos)`         | O(1)        |
| `insertar(pos, x)`     | O(n)        |
| `insertar_ordenado(x)` | O(n)        |
| `buscar_lineal(x)`     | O(n)        |
| `buscar_binaria(x)`    | O(log n)    |

## Lo que espero que pase en las mediciones

Creo que `obtener(pos)` va a mantenerse prácticamente igual aunque aumentemos el tamaño de la lista.

`insertar(pos, x)`, `insertar_ordenado(x)` y `buscar_lineal(x)` deberían tardar cada vez más cuando aumentemos la cantidad de elementos.

En cambio, espero que `buscar_binaria(x)` aumente muy poco su tiempo, porque en cada búsqueda va descartando aproximadamente la mitad de los elementos.

Estas son las predicciones que después voy a comprobar con las mediciones usando `timeit`.
