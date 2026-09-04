import csv
import matplotlib.pyplot as plt


datos = {}

with open("resultados.csv", "r") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        operacion = fila["operacion"]

        if operacion not in datos:
            datos[operacion] = {
                "n": [],
                "tiempo": []
            }

        datos[operacion]["n"].append(int(fila["n"]))
        datos[operacion]["tiempo"].append(float(fila["tiempo_medido"]))


for operacion in datos:
    plt.plot(
        datos[operacion]["n"],
        datos[operacion]["tiempo"],
        marker="o",
        label=operacion
    )


plt.xlabel("Cantidad de elementos")
plt.ylabel("Tiempo (segundos)")
plt.title("Tiempo de las operaciones de ListaArreglo")
plt.legend()
plt.grid(True)

plt.savefig("grafica_resultados.png")
plt.show()