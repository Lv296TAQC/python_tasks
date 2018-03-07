import logging
import pytest
from tasks.task_86g import total_sum1

logging.basicConfig(level=logging.WARNING,
                    format='# %(levelname)-8s [%(asctime)s] %(filename)-20s [LINE:%(lineno)s]   %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='logging.log',
                    filemode='w')


@pytest.mark.parametrize('a, b', [
    (133, 1),
    (6563, 4)
])
def test_total_sum(a, b):
    assert total_sum1(a) == b


@pytest.mark.parametrize('a', [
    (-2),
    ('ad'),
    ([1, 2, 3])
])
def test_total_sum_error1(a):
    with pytest.raises(ValueError):
        total_sum1(a)


def test_logging():
    assert total_sum1(133) == 2
    logging.WARNING('Error')


@pytest.mark.for_errors
def test_total_sum_error2():
    with pytest.raises(TypeError):
        total_sum1()
    print("Test passed")
