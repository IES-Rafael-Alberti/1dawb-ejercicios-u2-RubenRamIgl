import pytest
from src.Ejercicios2_1.Ejercicio2 import pedirContraseña, validarContraseña, igual

@pytest.mark.parametrize(
    "input_contraseña, input_pregunta, expected",
    [
        ("hola","hola", True),
        ("hola","adios", False),
        ("contraseña", "contraseña",True),
        
    ]
)
def test_igual_params(input_contraseña,input_pregunta, expected):
    assert igual(input_contraseña,input_pregunta) == expected