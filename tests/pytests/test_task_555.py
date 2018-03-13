import pytest
from task.task_555 import triagle


@pytest.mark.parametrize("input, expected", [
    (1, [[1]]),
    (2, [[1], [1, 1]]),
    (3, [[1], [1, 1], [1, 2, 1]])
])
def test_with_correct_value(input, expected):
    assert triagle(input) == expected


@pytest.mark.parametrize("input", [
    [1], (2,), {3: 4}, "s", 5.1
])
def test_with_incorrect_type(input):
    with pytest.raises(TypeError):
        triagle(input)
