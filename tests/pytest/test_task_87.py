import pytest
from tasks.task_87 import natural_number


@pytest.mark.parametrize('a, b, c', [
    (1234, 2, 7),
    (7200, 2, 0),
    (1510, 0, 0)
])
def test_normal_args(a, b, c):
    assert natural_number(a, b) == c


@pytest.mark.parametrize('a, b, c', [
    (1, 4, 1),
    (815, 4, 14)
])
def test_greater_second_arg(a, b, c):
    assert natural_number(a, b) == c


@pytest.mark.parametrize('a, b', [
    (-1234, 2),
    (557, -1),
    (5.57, 2),
    (3967, 8.9)
])
def test_unsuitable_num_args(a, b):
    with pytest.raises(ValueError):
        natural_number(a, b)


@pytest.mark.parametrize('a, b', [
    ('', 4),
    ('5dssa6578', 4),
    (8569, ''),
    (8569, '3'),
    ('d5fd5fd5', 't5')
])
def test_str_args(a, b):
    with pytest.raises(TypeError):
        natural_number(a, b)
