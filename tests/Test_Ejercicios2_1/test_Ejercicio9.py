import pytest
from src.Ejercicios2_1.Ejercicio9 import pedirEdad, definirPrecio

@pytest.mark.parametrize(
    "input_edad, expected",
    [
        (3, 0),
        (10, 5),
        (20, 10),
        (15, 5)
    ]
)
def test_definirPrecio_params(input_edad, expected):
    assert definirPrecio(input_edad) == expected