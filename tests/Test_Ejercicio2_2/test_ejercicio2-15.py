import pytest
from src.Ejercicios2_2.Ejercicio15 import sumarNumeros

@pytest.mark.parametrize(
    "input_n, expected",
    [
        ([4, 2], 6),
        ([5, 5], 10)
    ]
)
def test_sumarNumeros_params(input_n, expected):
    resultado = sumarNumeros(input_n[0])
    assert resultado == expected
