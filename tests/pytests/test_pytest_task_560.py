import pytest
from tasks.task_560 import amicable


def test_01_task_330():
    assert amicable() == [(220, 284)]


def test_02_task_330():
    with pytest.raises(TypeError):
        amicable('abc')


def test_03_task_330():
    with pytest.raises(TypeError):
        amicable({4: 1})


def test_04_task_330():
    with pytest.raises(TypeError):
        amicable([8])


def test_05_task_330():
    with pytest.raises(TypeError):
        amicable({6, })


def test_06_task_330():
    with pytest.raises(TypeError):
        amicable((8, ))
