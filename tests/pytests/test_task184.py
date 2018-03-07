import pytest

from tasks.task_184 import update


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
def test_update():
    assert update(23, 12, [233, 23, 23, 12]) == [233, 23, 23, 0]


@pytest.mark.for_errors
def test_update_raise():
    with pytest.raises(TypeError):
        update("qwe", -4, [12, 23])


@pytest.mark.skipif(True, reason=' some reason')
def test_update_none():
    with pytest.raises(TypeError):
        update('', ' ', [])
