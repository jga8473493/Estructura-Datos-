def crear_carrito():
    return []

def agregar(carrito, producto, cantidad):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a cero")
    for i, (prod, cant) in enumerate(carrito):
        if prod == producto:
            carrito[i] = (prod, cant + cantidad)
            return
    carrito.append((producto, cantidad))

def sacar(carrito, producto, cantidad):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor a cero")
    for i, (prod, cant) in enumerate(carrito):
        if prod == producto:
            if cant <= cantidad:
                carrito.pop(i)
            else:
                carrito[i] = (prod, cant - cantidad)
            return
    raise ValueError("Producto no encontrado")

def obtener_total_items(carrito):
    return sum(cant for _, cant in carrito)