# Decisión sobre mantener el catálogo ordenado
Para tomar la decisión voy a comparar cuánto cuesta hacer 50 búsquedas y 1 inserción.
Voy a comparar dos casos:
- Catálogo desordenado: búsqueda lineal + inserción.
- Catálogo ordenado: búsqueda binaria + inserción ordenada.
Los tiempos utilizados salen de las mediciones hechas con `timeit`.
# Con 80.000 registros
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
50 × 0.004378292 + 0.009350803
= 0.228265403 segundos

Con los resultados obtenidos, considero que sí conviene mantener el catálogo ordenado.
Aunque hacer una inserción ordenada toma un poco más de tiempo porque toca mover algunos elementos, la búsqueda binaria es mucho más rápida que la búsqueda lineal.
En el caso normal, donde se hacen unas 50 búsquedas por cada inserción, el tiempo total termina siendo mucho menor si el catálogo está ordenado.
Durante los exámenes, donde se realizan alrededor de 300 búsquedas por cada inserción, mantenerlo ordenado conviene todavía más, ya que se hacen muchas más búsquedas.
En las vacaciones, con solo unas 5 búsquedas por cada inserción, la diferencia es menor, pero según los resultados obtenidos también sigue siendo mejor mantenerlo ordenado.
Por lo tanto, mi decisión final es mantener el catálogo ordenado, ya que aunque las inserciones sean un poco más costosas, se ahorra bastante tiempo en las búsquedas.

