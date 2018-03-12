import pytest
from tasks.task_182 import sum_div5_notdiv7


def test_sum_div5_notdiv7(conf_func_fixture):
    assert sum_div5_notdiv7([5, 10, 107, 456]) == (15, 2)

@pytest.mark.for_errors
def test_sum_div5_notdiv7_errors():
    with pytest.raises(TypeError):
        sum_div5_notdiv7('qwerty')

@pytest.mark.for_errors
def test_sum_div5_notdiv7_errors2():
    with pytest.raises(TypeError):
        sum_div5_notdiv7()

@pytest.mark.for_errors
def test_sum_div5_notdiv7_errors3():
    with pytest.raises(KeyError):
        sum_div5_notdiv7({1:2})