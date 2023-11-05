import pytest
from src.Ejercicios2_1.Ejercicio5 import pedirEdad, pedirIngresos, tributa

@pytest.mark.parametrize(
    "input_edad, input_ingresos, expected",
    [
        (17, 800, False),
        (30, 2000, True),
        (15, 600, False)
        
    ]
)
def test_tributa_params(input_edad, input_ingresos, expected):
    assert tributa(input_edad,input_ingresos) == expected