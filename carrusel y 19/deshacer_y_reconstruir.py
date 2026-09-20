class Nodo:
    def __init__(self, estado):
        self.estado = estado
        self.prev = None
        self.next = None
class UndoRedoNodos:
    def __init__(self, estado_inicial):
        self.current = Nodo(estado_inicial)

    def hacer(self, nuevo_estado):
        nuevo_nodo = Nodo(nuevo_estado)
        
        # Conectamos el nodo nuevo hacia adelante y hacia atrás
        self.current.next = nuevo_nodo
        nuevo_nodo.prev = self.current
        
        # Movemos el puntero actual al nuevo nodo (el "futuro" se descarta)
        self.current = nuevo_nodo

    def undo(self):
        if self.current.prev is not None:
            self.current = self.current.prev
            return self.current.estado
        return None  # No hay más atrás

    def redo(self):
        if self.current.next is not None:
            self.current = self.current.next
            return self.current.estado
        return None  # No hay más adelante 
