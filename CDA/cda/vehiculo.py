# vehiculo.py
# Aquí vive TODO lo relacionado con "qué es un vehículo" y cómo se valida su placa.

# "re" es el módulo de Python para expresiones regulares (RegEx).
# Una RegEx es una "plantilla" que sirve para comprobar si un texto tiene cierto formato.
import re

# Lista de tipos que el usuario puede elegir (RF-10: lista fija, sin texto libre).
TIPOS_VALIDOS = ["carro", "moto", "ambulancia", "bomberos", "policia"]

# Tipos que tienen prioridad. Se incluye "policía" con tilde por si alguien la escribe así.
TIPOS_ESPECIALES = ["ambulancia", "bomberos", "policia", "policía"]

# --- Plantillas (RegEx) de placas colombianas ---
# ^        = el texto empieza aquí
# [A-Z]{3} = exactamente 3 letras mayúsculas
# \d{3}    = exactamente 3 números (\d significa "dígito")
# [A-Z]    = 1 letra mayúscula
# $        = el texto termina aquí
PLACA_CARRO = r"^[A-Z]{3}\d{3}$"      # Ejemplo válido: ABC123
PLACA_MOTO = r"^[A-Z]{3}\d{2}[A-Z]$"  # Ejemplo válido: ABC12D
# La "r" antes de las comillas significa "texto crudo": así Python no se confunde con las "\".


class Vehiculo:
    """Un vehículo que llega al CDA. Guarda sus datos y si es especial."""

    # __init__ se ejecuta solo cuando creamos un vehículo: Vehiculo("ABC123", "carro", ...)
    # "self" es el propio vehículo que se está creando.
    def __init__(self, placa, tipo, color, marca):
        # strip() quita espacios sobrantes; upper() pasa a mayúsculas; lower() a minúsculas.
        self.placa = placa.strip().upper()
        self.tipo = tipo.strip().lower()
        self.color = color.strip()
        self.marca = marca.strip()
        # Se calcula solo (RF-03): es True si el tipo está en la lista de especiales.
        self.es_especial = self.tipo in TIPOS_ESPECIALES

    # __str__ define cómo se ve el vehículo cuando hacemos print(vehiculo).
    def __str__(self):
        estado = "ESPECIAL" if self.es_especial else "normal"
        # La "f" antes de las comillas permite meter variables dentro de { }.
        return f"{self.placa} | {self.tipo} | {self.color} | {self.marca} | {estado}"


def validar_placa(tipo, placa):
    """Devuelve True si la placa tiene el formato colombiano correcto para ese tipo (RF-09)."""
    tipo = tipo.strip().lower()
    placa = placa.strip().upper()
    # Las motos tienen su propio formato; todo lo demás usa el de carro.
    patron = PLACA_MOTO if tipo == "moto" else PLACA_CARRO
    # fullmatch exige que TODO el texto cumpla la plantilla (no solo una parte).
    # Devuelve algo si coincide y None si no; por eso comparamos "is not None".
    return re.fullmatch(patron, placa) is not None
