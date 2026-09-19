class ListaArreglo:
    def __init__(self, capacidad_inicial=1000):
        self.capacidad = capacidad_inicial
        self.arreglo = [None] * self.capacidad
        self.tamano = 0

    def _redimensionar(self):
        self.capacidad *= 2
        nuevo_arreglo = [None] * self.capacidad

        for i in range(self.tamano):
            nuevo_arreglo[i] = self.arreglo[i]

        self.arreglo = nuevo_arreglo

    def obtener(self, pos):
        if pos < 0 or pos >= self.tamano:
            raise IndexError("Índice fuera de rango")

        return self.arreglo[pos]

    def insertar(self, pos, x):
        if pos < 0 or pos > self.tamano:
            raise IndexError("Índice fuera de rango")

        if self.tamano == self.capacidad:
            self._redimensionar()

        # Mover los elementos una posición hacia la derecha
        for i in range(self.tamano, pos, -1):
            self.arreglo[i] = self.arreglo[i - 1]

        self.arreglo[pos] = x
        self.tamano += 1

    def insertar_ordenado(self, x):
        if self.tamano == self.capacidad:
            self._redimensionar()

        pos = self.tamano - 1

        while pos >= 0 and self.arreglo[pos] > x:
            self.arreglo[pos + 1] = self.arreglo[pos]
            pos -= 1

        self.arreglo[pos + 1] = x
        self.tamano += 1

    def buscar_lineal(self, x):
        for i in range(self.tamano):
            if self.arreglo[i] == x:
                return i

        return -1

    def buscar_binaria(self, x):
        inicio = 0
        fin = self.tamano - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2

            if self.arreglo[medio] == x:
                return medio
            elif self.arreglo[medio] < x:
                inicio = medio + 1
            else:
                fin = medio - 1

        return -1

