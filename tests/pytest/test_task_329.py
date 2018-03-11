import pytest
from tasks.task_329 import sum_of_digits, main_func


@pytest.mark.parametrize('a, b', [
    (15, 6),
    (1, 1)
])
def test_sum_of_digits_normal_arg(a, b):
    assert sum_of_digits(a) == b


def test_sum_of_digits_negative_arg():
    assert sum_of_digits(-1) == -1


def test_sum_of_digits_str_arg():
    with pytest.raises(TypeError):
        sum_of_digits('5')


def test_main_func_normal_args():
    assert main_func(24, 36) == [6, 15]


def test_main_func_negative_args():
    with pytest.raises(ValueError):
        main_func(-100, 36)


@pytest.mark.parametrize('a, b', [
    ('21', 25),
    (21, '25'),
    ('21', '25')
])
def test_main_func_str_arg(a, b):
    with pytest.raises(TypeError):
        main_func(a, b)
        