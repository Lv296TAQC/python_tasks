import pytest
from tasks.task_332 import lagrange


@pytest.mark.parametrize("input, expected",
                         [(123, (11, 1, 1, 0)),
                          (100, (10, 0, 0, 0)),
                          (7398, (86, 1, 1, 0))
])
def test_lagrange(input, expected):
    assert lagrange(input ) == expected

@pytest.mark.run(after='test_lagrange_for_errors3')
@pytest.mark.for_errors
def test_lagrange_for_errors():
    with pytest.raises(TypeError):
        lagrange(-4)

@pytest.mark.run(order=2)
@pytest.mark.for_errors
def test_lagrange_for_errors2():
    with pytest.raises(TypeError):
        lagrange('qwerty')

@pytest.mark.run(order=1)
@pytest.mark.for_errors
def test_lagrange_for_errors3():
    with pytest.raises(TypeError):
        lagrange()