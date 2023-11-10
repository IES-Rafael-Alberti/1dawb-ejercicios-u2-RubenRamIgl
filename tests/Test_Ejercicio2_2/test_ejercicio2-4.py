import pytest
from src.Ejercicios2_2.Ejercicio4 import numeroPositivo, cuentaAtras

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (10, "10,9,8,7,6,5,4,3,2,1,0"),
        (5, "5,4,3,2,1,0"),
    ]
)
def test_cuentaAtras_params(input_n, expected):
    resultado=cuentaAtras(input_n)
    assert resultado == expected