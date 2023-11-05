import pytest
from src.Ejercicios2_1.Ejercicio3 import pedirNumero, pedirDivisor, division

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (2, 2, 1.00),
        (70, 3, 23.33),
        (400, 5, 80.00)
        
    ]
)
def test_division_params(input_n1, input_n2, expected):
    resultado = division(input_n1, input_n2)
    assert round(resultado, 2) == round(expected, 2)