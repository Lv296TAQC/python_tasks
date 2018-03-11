import pytest
from tasks.task_88 import three_go_in


@pytest.fixture(scope="module", autouse=False, params=[
                (19, True),
                (191, True),
                (6, True)
                ])
def param_test(request):
    return request.param


def test_00_task_88(param_test):
    (inputting, expected_output) = param_test
    result = three_go_in(inputting)
    assert result == expected_output


@pytest.mark.dependency(name="4", depends=["0", "3"])
@pytest.mark.run(order=7)
def test_01_task_88():
    assert three_go_in(19)


@pytest.mark.run(order=1)
def test_02_task_88():
    with pytest.raises(TypeError):
        three_go_in('abc')


@pytest.mark.dependency(name="3", depends=["0"])
@pytest.mark.run(order=6)
def test_03_task_88():
    with pytest.raises(TypeError):
        three_go_in((4, 3))


@pytest.mark.dependency(name="1")
def test_04_task_88():
    with pytest.raises(TypeError):
        three_go_in({14: 6})


@pytest.mark.dependency(name="0")
@pytest.mark.run(order=2)
def test_05_task_88():
    with pytest.raises(TypeError):
        three_go_in({8, 2})


@pytest.mark.dependency(name="2", depends=["1"])
def test_06_task_88():
    with pytest.raises(TypeError):
        three_go_in([1, 3])


@pytest.mark.run(order=1)
def test_07_task_88():
    with pytest.raises(TypeError):
        three_go_in()


@pytest.mark.xfail
def test_08_task_88_fail():
    assert three_go_in(2)


@pytest.mark.run(order=3)
@pytest.mark.skip("Why? Because I CAN! (Elisa, League Of Legends ref.)")
def test_09_task_88():
    with pytest.raises(TypeError):
        three_go_in("To be or not to be?")
