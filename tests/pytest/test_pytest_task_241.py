import pytest
import allure
from tasks.task_241 import difficult_formula, validate_values


@pytest.allure.step('step one')
@pytest.mark.for_errors
def test_difficult_formula_for_errors():
    with pytest.raises(TypeError):
        difficult_formula('qwerty')

@pytest.allure.step('make_some_data_foo')
def test_validate_values():
    assert validate_values(32, 34.5) == True
    assert validate_values(-32, 'qwerty') == False

@pytest.mark.skip
@pytest.mark.for_errors
def test_validate_values_for_errors():
    with pytest.raises(TypeError):
        validate_values()

@pytest.mark.for_errors
def test_validate_values_for_errors2():
    with pytest.raises(TypeError):
        validate_values(1)
