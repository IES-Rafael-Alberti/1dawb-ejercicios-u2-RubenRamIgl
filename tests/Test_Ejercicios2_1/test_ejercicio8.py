import pytest
from src.Ejercicios2_1.Ejercicio8 import pedirPuntuacion, definirNivel

@pytest.mark.parametrize(
    "input_puntuacion, expected_nivel, expected_dinero, expected_extra, expected_total",
    [
        (0.0, "Inaceptable", 2400, 0.0, 2400.0),
        (0.4, "Aceptable", 2400, 960.0, 3360.0),
        (0.6, "Meritorio", 2400, 1440.0, 3840.0),
        (1.0, "Meritorio", 2400, 2400.0, 4800.0)
    ]
)
def test_definirNivel_params(input_puntuacion, expected_nivel, expected_dinero, expected_extra, expected_total):
    nivel, dinero, extra, total = definirNivel(input_puntuacion)
    assert nivel == expected_nivel
    assert dinero == expected_dinero
    assert extra == expected_extra
    assert total == expected_total