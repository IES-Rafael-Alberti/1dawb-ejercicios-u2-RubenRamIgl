import pytest
from src.Ejercicios2_1.Ejercicio4 import pedirNumero, parImpar

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (2, True),
        (3, False),
        (8,True)
        
    ]
)
def test_parImpar_params(input_n, expected):
    assert parImpar(input_n) == expected
