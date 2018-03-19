import pytest
import logging
from tasks.task_88d import one_bounds, validate


logging.basicConfig(level=logging.INFO,
                    format='# %(levelname)-8s [%(asctime)s] %(filename)-20s [LINE:%(lineno)s]   %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='my_log.log',
                    filemode='w')

@pytest.allure.step('First step')
@pytest.mark.parametrize('input, expected',
                         [(0, 101),
                          (5, 151),
                          (10, 1101),
                          (15, 1151)],
                         ids=['for0', 'for5', 'for10', 'for15'
])
def test_one_bounds(input, expected):
    logging.info('Function one_bounds: Input - {}, actual result - {}, '
                 'expected result - {}'.format(input, one_bounds(input), expected))
    if one_bounds(input) != expected:
        logging.error('This test failed')
    assert one_bounds(input) == expected

@pytest.allure.step('Second step')
@pytest.mark.for_errors
def test_one_bounds_for_error():
    with pytest.raises(TypeError):
        one_bounds('qwerty')

@pytest.allure.step('Third step')
@pytest.mark.for_errors
def test_one_bounds_for_error():
    with pytest.raises(TypeError):
        one_bounds([])

@pytest.allure.step('Fourth step')
@pytest.mark.for_errors
def test_one_bounds_for_error2():
    with pytest.raises(TypeError):
        one_bounds()

@pytest.allure.step('Fifth step')
def test_validate():
    assert validate(12) == True

@pytest.allure.step('Sixth step')
@pytest.mark.parametrize('input, expected',
                         [('qwerty', False),
                          ({}, False),
                          ([], False)],
                         ids=['for_string', 'for_dict', 'for_list'
])
def test_validate_for_invalid(input, expected):
    logging.info('Function validate: Input - {}, actual result - {}, '
                 'expected result - {}'.format(input, validate(input), expected))
    assert validate(input) == expected
