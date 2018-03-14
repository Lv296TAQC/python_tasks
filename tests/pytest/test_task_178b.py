import pytest
from tasks.task_178_b import multiple_numbers


@pytest.mark.parametrize('a, b', [
    ([6, 21, 96, 110], 3),
    ([-110, 5, 78], 0),
    ([1, 8, 6, 1, 5, 78], 1)
])
def test_multiple_numbers_suitable_args(a, b):
    assert multiple_numbers(a) == b


@pytest.mark.parametrize('a', ['', '58, -64, 9, 11'])
def test_multiple_numbers_str_arg(a):
    with pytest.raises(TypeError):
        multiple_numbers(a)
