import pytest
from src.Ejercicios2_2.Ejercicio16 import pedirNumeros, numeroMayor

@pytest.mark.parametrize(
    "input_n, expected",
    [
        ("18675", "8"),
        ("24391", "9")
    ]
)
def test_digitoMayor_params(input_n, expected):
    assert numeroMayor(input_n) == expected