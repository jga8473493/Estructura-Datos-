edad = 25
nombre = "juan"
altura = 1.75
peso = 70.5
activo = True
CONSTANTES = 3.14


def verificar_edad(edad, activo):
    if edad >= 18 and activo:
        return "Es mayor de edad y está activo"
    else:
        return "No es mayor de edad o no está activo"
#operadores logicos : and, or, not, pyton 
#operadores relacionales : > < <= >= == != 
if edad >= 18 and activo:
    print("Es mayor de edad y está activo")
else:
    print("No es mayor de edad o no está activo")
if activo:
    print("Está activo")

#funciones:
def verificar_altura(altura):
    if altura >= 1.70:
        return "Es alto"
    return "No es alto"


def main():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    altura = float(input("Ingrese su altura en metros: "))
    peso = float(input("Ingrese su peso en kg: "))
    activo = input("¿Está activo? (si/no): ").lower() == "si"
    print(verificar_edad(edad, activo))
    print(verificar_altura(altura))
    print(f"Su IMC es: {peso / (altura ** 2):.2f}")


if __name__ == "__main__":
    main()

#asset para verificar todo 



# Código base — Semana 01
# Fuente: 01-Momento-1-Contrato-y-secuencia/01-Semana-01-Repaso-y-modelo-de-memoria/02-guia-de-laboratorio.html

def contar(lista):
    """Devuelve cuántos elementos tiene la lista. No uses len()."""
    pass


def suma(lista):
    """Devuelve la suma de los elementos. No uses sum()."""
    pass


def maximo(lista):
    """Devuelve el mayor elemento. Si la lista está vacía, devuelve None."""
    pass


def buscar(lista, valor):
    """Devuelve el índice de la primera aparición de valor, o -1 si no está."""
    pass


def invertida(lista):
    """Devuelve una NUEVA lista con los elementos en orden inverso.
    La lista original no debe modificarse."""
    pass


def invertir_en_sitio(lista):
    """Invierte la lista MODIFICANDO la original. No devuelve nada."""
    pass
