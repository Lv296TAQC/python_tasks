import pytest
import logging
from tasks.task_182 import sum_div5_notdiv7


logging.basicConfig(level=logging.INFO,
                    filename='my_log.log',
                    filemode='w')

logger = logging.getLogger("test_pytest_task_182")
logger.info('This is an informative message for test_pytest_task_182.py')

def test_sum_div5_notdiv7(conf_func_fixture):
    with pytest.allure.step('step one'):
        assert sum_div5_notdiv7([5, 10, 107, 456]) == (15, 2)

@pytest.mark.for_errors
def test_sum_div5_notdiv7_errors():
    pytest.allure.attach('My attachment', 'My example of using attachment')
    with pytest.raises(TypeError):
        sum_div5_notdiv7('qwerty')

@pytest.mark.for_errors
def test_sum_div5_notdiv7_errors2():
    with pytest.raises(TypeError):
        sum_div5_notdiv7()

@pytest.mark.for_errors
def test_sum_div5_notdiv7_errors3():
    with pytest.raises(KeyError):
        sum_div5_notdiv7({1:2})