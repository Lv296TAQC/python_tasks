import pytest
from tasks.task_325 import func4


@pytest.mark.parametrize("input, expected", [
    (87, [3, 29]),
    (345, [3, 5, 23]),
    (2355, [3, 5, 157])
])
def test_multiply_two_digits(input, expected):
    assert func4(input) == expected


def test_with_zero():
    assert func4(0) == []


def test_with_negative_number():
    assert func4(-100) == []


@pytest.mark.parametrize("arg", [
    [4], (5,), {6: 7}, "jjffj"
])
def test_with_incorrect_type(arg):
    with pytest.raises(TypeError):
        func4(input)
