import pytest
from tasks.task_329 import sum_of_digits, main_func


@pytest.mark.parametrize('a, b', [
    (15, 6),
    (1, 1),
    (0, 0),
    (-1, 1)
])
def test_sum_of_digits_suitable_args(a, b):
    assert sum_of_digits(a) == b


@pytest.mark.parametrize('a', [12.8, 0.0])
def test_sum_of_digits_unsuitable_args(a):
    with pytest.raises(ValueError):
        sum_of_digits(a)


def test_sum_of_digits_str_arg():
    with pytest.raises(TypeError):
        sum_of_digits('5')


@pytest.mark.parametrize('a, b, c', [
    (24, 36, [6, 15]),
    (-24, 36, []),
    (3, 4, []),
    (36, 36, []),
    (0, 0, [])

])
def test_main_func_suitable_args(a, b, c):
    assert main_func(a, b) == c


@pytest.mark.parametrize('a, b', [
    (-100, 36),
    (100, -1),
    (-5, -18),
    (24.0, 36),
    (10, 4.5),
    (856.5, 422.1)
])
def test_main_func_unsuitable_args(a, b):
    with pytest.raises(ValueError):
        main_func(a, b)


@pytest.mark.parametrize('a, b', [
    ('21', 25),
    (21, '25'),
    ('21', '25')
])
def test_main_func_str_arg(a, b):
    with pytest.raises(TypeError):
        main_func(a, b)
