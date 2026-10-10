"""Prueba de humo de la Entrega 1: el repositorio arranca y pytest corre."""
import main


def test_main_importa():
    """Verifica que main.py se importa sin errores (requisito de repositorio)."""
    assert callable(main.main)
