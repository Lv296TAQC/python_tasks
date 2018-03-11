import pytest
from tasks.task_227 import comparison, divisor


def test_task_227_comparison():
    assert comparison(18, 6) == [-6, -3, -2, -1, 1, 2, 3, 6]
    with pytest.raises(TypeError):
        comparison('abc', 2)
    with pytest.raises(TypeError):
        comparison(3, {})
    with pytest.raises(TypeError):
        comparison(8, None)
    with pytest.raises(TypeError):
        comparison(None, None)
    with pytest.raises(TypeError):
        comparison(5, [])


def test_01_task_227_divisor():
    assert divisor(6) == [1, 2, 3, 6]


def test_02_task_227_divisor():
    with pytest.raises(TypeError):
        divisor('abc')


def test_03_task_227_divisor():
    with pytest.raises(TypeError):
        divisor()


def test_04_task_227_divisor():
    with pytest.raises(TypeError):
        divisor({4: 1})


def test_05_task_227_divisor():
    with pytest.raises(TypeError):
        divisor([8])


def test_06_task_227_divisor():
    with pytest.raises(TypeError):
        divisor({6, })


def test_07_task_227_divisor():
    with pytest.raises(TypeError):
        divisor((8, ))
