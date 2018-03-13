import pytest
from tasks.task_86b import sum_of_digits


@pytest.mark.parametrize("input, expected", [
    (12, 3),
    (123, 6),
    (12345, 15)
])
def test_sum_of_digits(input, expected):
    assert sum_of_digits(input) == expected


def test_sum_with_zeroes_and_one():
    assert sum_of_digits(1000) == 1


def test_sum_with_zero():
    assert sum_of_digits(0) == 0


def test_sum_with_minus_one():
    with pytest.raises(ValueError):
        sum_of_digits(-1)


def test_sum_with_str():
    with pytest.raises(ValueError):
        sum_of_digits('sad')


def test_sum_of_float():
    with pytest.raises(ValueError):
        sum_of_digits(15.78)


def test_with_several_args():
    with pytest.raises(TypeError):
        sum_of_digits(5, 10)


@pytest.mark.parametrize("arg", [
    [], (), {}
])
def test_with_incorrect_empty_type(arg):
    with pytest.raises(ValueError):
        sum_of_digits(input)


@pytest.mark.parametrize("value", [
    [1], (2,), {1: 5}
])
def test_with_incorrect_empty_type(value):
    with pytest.raises(ValueError):
        sum_of_digits(input)
