import pytest
import allure
from tasks.task_330 import minus_last, ideal


@pytest.mark.usefixtures("mock_divisor_value")
def test_01_task_330_minus_last():
    assert minus_last(6) == 6


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
def test_02_task_330_minus_last():
    with pytest.raises(TypeError):
        minus_last('abc')


@pytest.allure.step
def test_03_task_330_minus_last():
    with pytest.raises(TypeError):
        minus_last()


@pytest.allure.BLOCKER
def test_04_task_330_minus_last():
    with pytest.raises(TypeError):
        minus_last({4: 1})


def test_05_task_330_minus_last():
    with pytest.raises(TypeError):
        minus_last([8])
    allure.attach('tasks.task_330', 'My attach file')


def test_06_task_330_minus_last():
    with pytest.raises(TypeError):
        minus_last({6, })


def test_07_task_330_minus_last():
    with pytest.raises(TypeError):
        minus_last((8, ))


def test_01_task_330_ideal():
    assert ideal(501) == [6, 28, 496]


def test_02_task_330_ideal():
    with pytest.raises(TypeError):
        ideal('abc')


def test_03_task_330_ideal():
    with pytest.raises(TypeError):
        ideal((8,))


def test_04_task_330_ideal():
    with pytest.raises(TypeError):
        ideal({4: 1})


def test_05_task_330_ideal():
    with pytest.raises(TypeError):
        ideal([8])


def test_06_task_330_ideal():
    with pytest.raises(TypeError):
        minus_last({6, })
