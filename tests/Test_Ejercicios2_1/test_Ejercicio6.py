import pytest
from src.Ejercicios2_1.Ejercicio6 import pedirNombre, pedirSexo, asignarGrupo

@pytest.mark.parametrize(
    "input_nombre, input_sexo, expected",
    [
        ("Alejandro", "M", "B"),
        ("Ana", "F", "A"),
        ("Antonio", "M", "B"),
        ("Sara", "F", "B")
    ]
)
def test_asignarGrupo_params(input_nombre, input_sexo, expected):
    assert asignarGrupo(input_nombre, input_sexo) == expected