import pytest
from tasks.task_242 import total_sum


@pytest.mark.parametrize('a, b', [
    (1, 2.0),
    (4, 1.375),
    (7, 1.3817460317460317),
    (10, 1.3817733134920636)
])
def test_params(a, b):
    assert total_sum(a) == b


@pytest.mark.parametrize('a', [
    ([23]),
    ('qwe'),
    ()

])
def test_params_raise(a):
    with pytest.raises(TypeError):
        total_sum(a)
