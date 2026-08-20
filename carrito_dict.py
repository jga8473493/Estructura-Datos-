def crear_carrito():
    return {}

def agregar(carrito, producto, cantidad):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a cero")
    carrito[producto] = carrito.get(producto, 0) + cantidad

def sacar(carrito, producto, cantidad):
    if producto not in carrito:
        raise ValueError("Producto no encontrado")
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a cero")
    
    if carrito[producto] <= cantidad:
        del carrito[producto]
    else:
        carrito[producto] -= cantidad

def obtener_total_items(carrito):
    return sum(carrito.values())