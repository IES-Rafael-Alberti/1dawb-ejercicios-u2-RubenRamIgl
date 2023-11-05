import pytest
from src.Ejercicios2_2.Ejercicio17 import pedirDigitos, digitoMayor

@pytest.mark.parametrize(
    "input_digitos, expected",
    [
        ("97685", "9"),
        ("52453", "5")
    ]
)
def test_digitoMayor_params(input_digitos, expected):
    assert digitoMayor(input_digitos) == expected