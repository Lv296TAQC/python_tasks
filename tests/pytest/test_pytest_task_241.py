import pytest
import logging
from tasks.task_241 import difficult_formula, validate_values


logging.basicConfig(level=logging.INFO,
                    format='# %(levelname)-8s [%(asctime)s] %(filename)-20s [LINE:%(lineno)s]   %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='my_log.log',
                    filemode='w')

@pytest.allure.step('step one')
@pytest.mark.for_errors
def test_difficult_formula_for_errors():
    with pytest.raises(TypeError):
        difficult_formula('qwerty')

@pytest.allure.step('step two')
def test_validate_values_for_true():
    logging.info('Lets test validate_values function for True')
    assert validate_values(32, 34.5) == True

@pytest.allure.step('three')
def test_validate_values_for_false():
    logging.info('Lets test validate_values function for False')
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
