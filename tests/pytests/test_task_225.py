import pytest
from tasks.task_225 import func3


@pytest.mark.parametrize("input, expected", [
    (50, [5]),
    (324, [2, 6, 9, 18]),
    (3456, [8, 24])
])
def test_list_from_natural_number(input, expected):
    assert func3(input) == expected


def test_list_from_zero():
    assert func3(0) == []


def test_sum_with_str():
    with pytest.raises(TypeError):
        func3("gewg")


@pytest.mark.parametrize("arg", [
    [3], (7,), {8: 1}
])
def test_with_incorrect_type(arg):
    with pytest.raises(TypeError):
        func3(input)


@pytest.mark.parametrize("arg", [
    [], (), {}
])
def test_with_incorrect_empty_type(arg):
    with pytest.raises(TypeError):
        func3(arg)
