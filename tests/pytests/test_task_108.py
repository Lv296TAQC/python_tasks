import pytest
from task.task_108 import func2


@pytest.mark.parametrize("input, expected", [
    (1, 2),
    (15, 16),
    (250, 256)
])
def test_with_natural_number(input, expected):
    assert func2(input) == expected


def test_with_zero():
    assert func2(0) == 2


def test_with_str():
    with pytest.raises(TypeError):
        func2('fadsf')


@pytest.mark.parametrize("input", [
    [], (), {}
])
def test_with_incorrect_empty_type(input):
    with pytest.raises(TypeError):
        func2(input)


@pytest.mark.parametrize("input", [
    [3], (5,), {1: 8}
])
def test_with_incorrect_type(input):
    with pytest.raises(TypeError):
        func2(input)
