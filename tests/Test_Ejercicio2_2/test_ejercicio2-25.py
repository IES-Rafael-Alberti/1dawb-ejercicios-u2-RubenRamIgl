import pytest
from src.Ejercicios2_2.Ejercicio25 import pedirFrase, palabraLarga, contarLetras

@pytest.mark.parametrize(
    "input_frase, expected",
    [
        ("Hola mundo", 5),
        ("Esta es una prueba", 6),
        ("Una frase", 5),
        ("Frase más larga", 5)
    ]
)
def test_contarLetras_params(input_frase, expected):
    assert contarLetras(input_frase) == expected