import pytest
from src.Ejercicios2_2.Ejercicio14 import sumarNumeros

@pytest.mark.parametrize(
    "input_n, expected",
    [
        ([8, 2], 10),
        ([30, 25], 55)
    ]
)
def test_sumarNumeros_params(input_n, expected):
    resultado = sumarNumeros(input_n[0])
    assert resultado == expected