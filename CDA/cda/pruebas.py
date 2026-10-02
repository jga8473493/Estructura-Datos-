# pruebas.py
# Pruebas automáticas: una por cada criterio de aceptación (CA) de requirements.md (RNF-04).
# Se ejecuta con:  python pruebas.py
# Cada línea dice OK (funciona) o FALLA (hay un error en la lógica).

from vehiculo import Vehiculo, validar_placa
from cola_cda import ColaCDA


def nuevo(placa, tipo="carro"):
    """Crea un vehículo de prueba rápido (color y marca no importan aquí)."""
    return Vehiculo(placa, tipo, "rojo", "Mazda")


def probar(nombre, condicion):
    """Imprime OK si la condición es verdadera y FALLA si no."""
    print(("OK    " if condicion else "FALLA ") + nombre)


# CA-01 y CA-11: registrar y contar
c = ColaCDA()
probar("CA-01 registrar", c.registrar(nuevo("AAA111")))
c.registrar(nuevo("BBB222"))
probar("CA-11 contar pendientes", c.pendientes() == 2)

# CA-02: placa duplicada (debe devolver False)
probar("CA-02 placa duplicada", c.registrar(nuevo("AAA111")) is False)

# CA-03: identificar especial
probar("CA-03 es especial", nuevo("CCC333", "ambulancia").es_especial)

# CA-04: el especial pasa primero, aunque llegó después del normal
c = ColaCDA()
c.registrar(nuevo("N1"))
c.registrar(nuevo("E1", "bomberos"))
probar("CA-04 especial primero", c.siguiente().placa == "E1")

# CA-05: entre especiales, el que llegó primero
c.registrar(nuevo("E2", "policia"))
probar("CA-05 orden entre especiales", c.siguiente().placa == "E1")

# CA-06: entre normales, el que llegó primero
c = ColaCDA()
c.registrar(nuevo("N1"))
c.registrar(nuevo("N2"))
probar("CA-06 orden entre normales", c.siguiente().placa == "N1")

# CA-07: consultar el siguiente NO lo saca de la cola
c.siguiente()
probar("CA-07 siguiente no retira", c.pendientes() == 2)

# CA-08: cola vacía al consultar (debe devolver None)
probar("CA-08 cola vacía (siguiente)", ColaCDA().siguiente() is None)

# CA-09: atender retira al primero y el siguiente conserva su orden
c.atender()
probar("CA-09 atender retira", c.pendientes() == 1 and c.siguiente().placa == "N2")

# CA-10: cola vacía al atender
probar("CA-10 cola vacía (atender)", ColaCDA().atender() is None)

# CA-12: validación de placas colombianas ("not" = debe ser inválida)
probar("CA-12 carro válido", validar_placa("carro", "ABC123"))
probar("CA-12 carro inválido", not validar_placa("carro", "ABC12D"))
probar("CA-12 moto válida", validar_placa("moto", "ABC12D"))
probar("CA-12 moto inválida", not validar_placa("moto", "ABC123"))

# CA-13 y CA-14: retirar por placa
c = ColaCDA()
c.registrar(nuevo("N1"))
c.registrar(nuevo("N2"))
probar("CA-13 retirar por placa", c.retirar("N1") is not None and c.siguiente().placa == "N2")
probar("CA-14 placa inexistente", c.retirar("ZZZ999") is None)
