# cola_cda.py
# Aquí está la LÓGICA del CDA: las filas, la prioridad y las operaciones.
# No tiene pantallas ni menús: solo reglas. Por eso la usan main.py, interfaz.py y pruebas.py.

# deque = "fila" optimizada. Sacar el primero (popleft) es instantáneo.
# Una lista normal es más lenta porque mueve todos los elementos al sacar el primero (RNF-02).
from collections import deque


class ColaCDA:
    def __init__(self):
        self.cola_especiales = deque()  # Fila 1: ambulancias, bomberos, policía
        self.cola_normales = deque()    # Fila 2: carros y motos normales
        # set = conjunto: guarda placas SIN repetir y buscar en él es muy rápido.
        # Sirve para saber al instante si una placa ya está en espera.
        self.placas_pendientes = set()

    # T-03: registrar (RF-01, RF-02, RF-03)
    def registrar(self, vehiculo):
        if vehiculo.placa in self.placas_pendientes:
            return False  # Placa repetida: se rechaza
        # El vehículo se forma al final de SU fila (append = agregar al final).
        if vehiculo.es_especial:
            self.cola_especiales.append(vehiculo)
        else:
            self.cola_normales.append(vehiculo)
        self.placas_pendientes.add(vehiculo.placa)
        return True

    # T-04: ver quién sigue SIN sacarlo (RF-04, RF-05, RF-06)
    def siguiente(self):
        # [0] es el primero de la fila. Primero se mira la de especiales: esa es la PRIORIDAD.
        if self.cola_especiales:
            return self.cola_especiales[0]
        if self.cola_normales:
            return self.cola_normales[0]
        return None  # None = "nada". Significa que no hay vehículos.

    # T-05: atender = sacar de la fila al que sigue (RF-07)
    def atender(self):
        # popleft() saca y devuelve el primero de la fila.
        if self.cola_especiales:
            vehiculo = self.cola_especiales.popleft()
        elif self.cola_normales:
            vehiculo = self.cola_normales.popleft()
        else:
            return None
        # Ya no está en espera: su placa se puede volver a registrar más adelante.
        self.placas_pendientes.remove(vehiculo.placa)
        return vehiculo

    # T-06: cuántos faltan por atender (RF-08)
    def pendientes(self):
        return len(self.cola_especiales) + len(self.cola_normales)

    # T-10: sacar a un vehículo por su placa, sin atenderlo (RF-11)
    def retirar(self, placa):
        placa = placa.strip().upper()
        if placa not in self.placas_pendientes:
            return None  # Esa placa no está en la cola
        # Se busca en las dos filas hasta encontrarla.
        for cola in (self.cola_especiales, self.cola_normales):
            for v in cola:
                if v.placa == placa:
                    cola.remove(v)  # Los demás conservan su orden (CA-13)
                    self.placas_pendientes.remove(placa)
                    return v

    # T-11: lista completa en orden de atención. La usa la interfaz para dibujar la tabla.
    # list(...) convierte cada deque en lista y el "+" las une: primero especiales, luego normales.
    def ordenados(self):
        return list(self.cola_especiales) + list(self.cola_normales)
