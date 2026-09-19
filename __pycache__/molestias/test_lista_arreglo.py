from lista_arreglo import ListaArreglo


def test_lista_vacia():
    lista = ListaArreglo()

    assert lista.tamano == 0


def test_un_elemento():
    lista = ListaArreglo()

    lista.insertar(0, "Libro 1")

    assert lista.obtener(0) == "Libro 1"
    assert lista.tamano == 1


def test_insertar_al_inicio():
    lista = ListaArreglo()

    lista.insertar(0, "Libro 1")
    lista.insertar(0, "Libro 2")

    assert lista.obtener(0) == "Libro 2"
    assert lista.obtener(1) == "Libro 1"


def test_insertar_al_final():
    lista = ListaArreglo()

    lista.insertar(0, "Libro 1")
    lista.insertar(1, "Libro 2")
    lista.insertar(2, "Libro 3")

    assert lista.obtener(0) == "Libro 1"
    assert lista.obtener(1) == "Libro 2"
    assert lista.obtener(2) == "Libro 3"


def test_insertar_en_medio():
    lista = ListaArreglo()

    lista.insertar(0, "Libro 1")
    lista.insertar(1, "Libro 3")
    lista.insertar(1, "Libro 2")

    assert lista.obtener(0) == "Libro 1"
    assert lista.obtener(1) == "Libro 2"
    assert lista.obtener(2) == "Libro 3"


def test_insertar_ordenado():
    lista = ListaArreglo()

    lista.insertar_ordenado(30)
    lista.insertar_ordenado(10)
    lista.insertar_ordenado(20)

    assert lista.obtener(0) == 10
    assert lista.obtener(1) == 20
    assert lista.obtener(2) == 30


def test_buscar_lineal():
    lista = ListaArreglo()

    lista.insertar(0, 10)
    lista.insertar(1, 20)
    lista.insertar(2, 30)

    assert lista.buscar_lineal(10) == 0
    assert lista.buscar_lineal(20) == 1
    assert lista.buscar_lineal(30) == 2
    assert lista.buscar_lineal(50) == -1


def test_buscar_binaria():
    lista = ListaArreglo()

    lista.insertar_ordenado(10)
    lista.insertar_ordenado(20)
    lista.insertar_ordenado(30)
    lista.insertar_ordenado(40)
    lista.insertar_ordenado(50)

    assert lista.buscar_binaria(10) == 0
    assert lista.buscar_binaria(30) == 2
    assert lista.buscar_binaria(50) == 4
    assert lista.buscar_binaria(100) == -1


def test_obtener_fuera_de_rango():
    lista = ListaArreglo()

    try:
        lista.obtener(0)
        assert False
    except IndexError:
        assert True


def test_insertar_posicion_invalida():
    lista = ListaArreglo()

    try:
        lista.insertar(1, "Libro")
        assert False
    except IndexError:
        assert True
