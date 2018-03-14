import pytest
from tasks.task_226 import common_multiple


@pytest.mark.parametrize('a, b, c', [
    (12, 22, 132),
    (1, 1, 1)
])
def test_common_multiple_suitable_args(a, b, c):
    assert common_multiple(a, b) == c


@pytest.mark.parametrize('a, b', [
    (-134, 2),
    (12, -1)
])
def test_common_multiple_unsuitable_args(a, b):
    with pytest.raises(ValueError):
        common_multiple(a, b)


@pytest.mark.parametrize('a, b', [
    ('', 4),
    ('5dssa6578', 4),
    (8569, ''),
    (8569, '3')
])
def test_common_multiple_str_args(a, b):
    with pytest.raises(TypeError):
        common_multiple(a, b)
