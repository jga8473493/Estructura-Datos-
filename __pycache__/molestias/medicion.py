import timeit
import statistics
import csv
from lista_arreglo import ListaArreglo


TAMANOS = [1000, 10000, 80000, 200000]
REPETICIONES = 5


def crear_lista(n):
    lista = ListaArreglo(capacidad_inicial=n)

    for i in range(n):
        lista.arreglo[i] = i

    lista.tamano = n
    return lista


def medir_obtener(n):
    lista = crear_lista(n)

    tiempos = timeit.repeat(
        lambda: lista.obtener(n // 2),
        repeat=REPETICIONES,
        number=1
    )

    return statistics.median(tiempos)


def medir_insertar(n):
    lista = crear_lista(n)

    tiempos = timeit.repeat(
        lambda: lista.insertar(0, -1),
        repeat=REPETICIONES,
        number=1
    )

    return statistics.median(tiempos)


def medir_insertar_ordenado(n):
    lista = crear_lista(n)

    tiempos = timeit.repeat(
        lambda: lista.insertar_ordenado(-1),
        repeat=REPETICIONES,
        number=1
    )

    return statistics.median(tiempos)


def medir_buscar_lineal(n):
    lista = crear_lista(n)

    tiempos = timeit.repeat(
        lambda: lista.buscar_lineal(n - 1),
        repeat=REPETICIONES,
        number=1
    )

    return statistics.median(tiempos)


def medir_buscar_binaria(n):
    lista = crear_lista(n)

    tiempos = timeit.repeat(
        lambda: lista.buscar_binaria(n - 1),
        repeat=REPETICIONES,
        number=1
    )

    return statistics.median(tiempos)


def main():
    resultados = []

    for n in TAMANOS:
        print("Midiendo", n, "elementos...")

        resultados.append([
            n,
            "obtener",
            medir_obtener(n)
        ])

        resultados.append([
            n,
            "insertar",
            medir_insertar(n)
        ])

        resultados.append([
            n,
            "insertar_ordenado",
            medir_insertar_ordenado(n)
        ])

        resultados.append([
            n,
            "buscar_lineal",
            medir_buscar_lineal(n)
        ])

        resultados.append([
            n,
            "buscar_binaria",
            medir_buscar_binaria(n)
        ])

    with open("resultados.csv", "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["n", "operacion", "tiempo_medido"])

        for resultado in resultados:
            escritor.writerow(resultado)

    print("Mediciones terminadas.")
    print("Los resultados se guardaron en resultados.csv")


if __name__ == "__main__":
    main()