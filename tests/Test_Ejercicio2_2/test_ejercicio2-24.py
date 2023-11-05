import pytest
from src.Ejercicios2_2.Ejercicio24 import pedirNumeros, esPrimo, contarPrimos

@pytest.mark.parametrize(
    "input_numeros, expected",
    [
        ([2, 3, 5, 7, 11], 5),  # Lista con 5 números primos
        ([4, 6, 8, 9, 10], 0),  # Lista sin números primos
        ([2, 3, 5, 6, 7], 4),  # Lista con 4 números primos
        ([11, 13, 17, 19, 23, 29], 6),  # Lista con 6 números primos
        ([4, 6, 8, 9, 10], 0),  # Lista sin números primos
        ([97, 101, 103], 3),  # Lista con 3 números primos
    ]
)
def test_contarPrimos_params(input_numeros, expected):
    assert contarPrimos(input_numeros) == expected
