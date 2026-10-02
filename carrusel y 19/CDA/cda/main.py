# main.py
# Menú de CONSOLA (texto). Se ejecuta con:  python main.py
# Solo pide datos y muestra resultados; la lógica real está en cola_cda.py.

from vehiculo import Vehiculo, TIPOS_VALIDOS, validar_placa
from cola_cda import ColaCDA

cda = ColaCDA()  # Creamos el CDA (las filas empiezan vacías)

# Texto del menú. Las comillas triples """ permiten escribir varias líneas.
# OJO: los números de aquí deben coincidir con los "if opcion ==" de más abajo.
MENU = """
===== CDA =====
1. Registrar vehículo
2. Ver siguiente
3. Atender vehículo
4. Retirar vehículo de la cola
5. Ver pendientes
6. Salir
"""


def pedir_tipo():
    """Muestra los tipos numerados y pide un número (así no se puede escribir cualquier cosa)."""
    print("Tipo de vehículo:")
    # enumerate(lista, 1) da el número (empezando en 1) y el elemento: (1, "carro"), (2, "moto")...
    for i, t in enumerate(TIPOS_VALIDOS, 1):
        print(f"  {i}. {t}")
    while True:  # Se repite hasta que el usuario elija bien
        op = input("Elija el número: ").strip()
        # isdigit() comprueba que sean solo números; luego se verifica que esté en el rango.
        if op.isdigit() and 1 <= int(op) <= len(TIPOS_VALIDOS):
            return TIPOS_VALIDOS[int(op) - 1]  # -1 porque las listas empiezan en 0
        print("Opción no válida.")


def pedir_placa(tipo):
    """Pide la placa hasta que tenga el formato colombiano correcto."""
    ejemplo = "ABC12D" if tipo == "moto" else "ABC123"
    while True:
        placa = input(f"Placa (ej. {ejemplo}): ").strip().upper()
        if validar_placa(tipo, placa):
            return placa
        print(f"Placa inválida para {tipo}. Ejemplo: {ejemplo}")


def pedir_texto(nombre, solo_letras=False):
    """Pide un texto obligatorio. Si solo_letras=True, no acepta números (para el color)."""
    while True:
        texto = input(f"{nombre}: ").strip()
        if not texto:
            print(f"{nombre} es obligatorio.")
        # replace quita los espacios para que "azul claro" también cuente como solo letras.
        elif solo_letras and not texto.replace(" ", "").isalpha():
            print(f"{nombre} solo admite letras.")
        else:
            return texto


def ejecutar_menu():
    """Bucle principal del menú de consola."""
    while True:
        print(MENU)
        opcion = input("Opción: ").strip()

        if opcion == "1":
            # Orden de los campos: tipo, placa, marca, color (RNF-05)
            tipo = pedir_tipo()
            placa = pedir_placa(tipo)
            marca = pedir_texto("Marca")
            color = pedir_texto("Color", solo_letras=True)
            if cda.registrar(Vehiculo(placa, tipo, color, marca)):
                print("Vehículo registrado.")
            else:
                print("Esa placa ya está pendiente de atención.")

        elif opcion == "2":
            v = cda.siguiente()
            # Si v tiene algo se muestra; si es None (vacío) se muestra el aviso.
            print(f"Siguiente: {v}" if v else "No hay vehículos pendientes.")

        elif opcion == "3":
            v = cda.atender()
            print(f"Atendido: {v}" if v else "No hay vehículos pendientes.")

        elif opcion == "4":
            placa = input("Placa a retirar: ")
            v = cda.retirar(placa)
            print(f"Retirado: {v}" if v else "Esa placa no está en la cola.")

        elif opcion == "5":
            print(f"Pendientes: {cda.pendientes()}")

        elif opcion == "6":
            print("Hasta luego.")
            break  # Rompe el bucle y el programa termina

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    ejecutar_menu()
