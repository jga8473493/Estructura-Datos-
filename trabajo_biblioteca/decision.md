# Decisión sobre mantener el catálogo ordenado
Para tomar la decisión voy a comparar cuánto cuesta hacer 50 búsquedas y 1 inserción.
Voy a comparar dos casos:
- Catálogo desordenado: búsqueda lineal + inserción.
- Catálogo ordenado: búsqueda binaria + inserción ordenada.
Los tiempos utilizados salen de las mediciones hechas con `timeit`.
## Con 80.000 registros
Búsqueda lineal:
0.004378292 segundos
Búsqueda binaria:
0.000003425 segundos
Inserción:
0.009350803 segundos
Inserción ordenada:
0.020528100 segundos
### Catálogo desordenado
50 búsquedas lineales + 1 inserción:
catalogo_ordenado_:
50 × 0.004378292 + 0.009350803
= 0.228265403 segundos