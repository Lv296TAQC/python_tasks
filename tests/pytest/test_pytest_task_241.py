import pytest
from tasks.task_241 import difficult_formula, validate_values


def test_difficult_formula():
    assert difficult_formula(44, 2.5) == -3076222890240854.5 + 1.1630684374642796e+16j

@pytest.mark.for_errors
def test_difficult_formula_for_errors():
    with pytest.raises(TypeError):
        difficult_formula('qwerty')

def test_validate_values():
    assert validate_values(32, 34.5) == True
    assert validate_values(-32, 'qwerty') == False

@pytest.mark.for_errors
def test_validate_values_for_errors():
    with pytest.raises(TypeError):
        validate_values()

@pytest.mark.for_errors
def test_validate_values_for_errors2():
    with pytest.raises(TypeError):
        validate_values(1)
