import pytest
from src.Ejercicios2_2.Ejercicio18 import pedirNumeros, sumarNumeros, contarPares

@pytest.mark.parametrize(
    "input_numeros, expected",
    [
        ([1, 2, 3, 4, 5], 15),
        ([], 0),
        ([7, 9, 11], 27),
        ([0, 0, 0, 0], 0)
    ]
)
def test_sumarNumeros_params(input_numeros, expected):
    assert sumarNumeros(input_numeros) == expected
    
@pytest.mark.parametrize(
    "input_numeros, expected",
    [
        ([1, 2, 3, 4, 5], 2),
        ([], 0),
        ([7, 9, 11], 0),
        ([0, 0, 0, 0], 4)
    ]
)
def test_contarPares_params(input_numeros, expected):
    assert contarPares(input_numeros) == expected