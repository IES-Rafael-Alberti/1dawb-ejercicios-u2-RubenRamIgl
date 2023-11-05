import pytest
from src.Ejercicios2_1.Ejercicio10 import pedirTipo, pedirIngredientes

@pytest.mark.parametrize(
    "input_tipo, expected_pizza, expected_ingrediente",
    [
        ("si", "vegetariana", "pimiento"),
        ("no", "no vegetariana", "peperoni")
    ]
)
def test_pedirIngredientes_params(input_tipo, expected_pizza, expected_ingrediente, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: input_tipo)
    
    pizza, ingrediente = pedirIngredientes(input_tipo)
    assert pizza == expected_pizza
    assert ingrediente == expected_ingrediente

    