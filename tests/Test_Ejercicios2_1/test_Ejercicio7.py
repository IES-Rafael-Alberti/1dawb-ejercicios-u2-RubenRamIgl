import pytest
from src.Ejercicios2_1.Ejercicio7 import pedirRenta, impositivo

@pytest.mark.parametrize(
    "input_renta, expected",
    [
        (5000, 5),
        (50000, 30),
        (25000, 20),
        (65000, 45)
    ]
)
def test_impositivo_params(input_renta, expected):
    assert impositivo(input_renta) == expected