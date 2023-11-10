import pytest
from src.Ejercicios2_2.Ejercicio12 import pedirFrase, pedirLetra, contarLetra

@pytest.mark.parametrize(
    "input_frase, input_letra, expected",
    [
        ("hola que tal", "l", 2),
        ("hola mundo", "o", 2),
        ("esto es un test", "z", 0),
    ]
)
def test_contarLetra_params(input_frase, input_letra, expected):
    resultado = contarLetra(input_frase, input_letra)
    assert resultado == expected