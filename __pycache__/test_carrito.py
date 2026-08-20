import pytest
import carrito_dict as car

def test_carrito_vacio():
    c = car.crear_carrito()
    assert car.obtener_total_items(c) == 0

def test_agregar_y_total():
    c = car.crear_carrito()
    car.agregar(c, "Manzana", 3)
    assert car.obtener_total_items(c) == 3

def test_cantidad_invalida():
    c = car.crear_carrito()
    with pytest.raises(ValueError):
        car.agregar(c, "Manzana", 0)

def test_sacar_inexistente():
    c = car.crear_carrito()
    with pytest.raises(ValueError):
        car.sacar(c, "Pera", 1)