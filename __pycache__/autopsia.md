# Autopsia del Error de Alias en Memoria

## Diagnóstico del Error
El problema ocurre porque ambas cajas comparten la misma referencia a un objeto mutable en la memoria Heap. Esto sucede al definir un parámetro mutable por defecto en Python:

```python
class Caja:
    def __init__(self, carrito=[]):  # La lista se crea una sola vez al definir la clase
        self.carrito = carrito

class Caja:
    def __init__(self, carrito=None):
        if carrito is None:
            self.carrito = []  # Nueva instancia en Heap
        else:
            self.carrito = list(carrito)