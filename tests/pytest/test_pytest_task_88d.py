import pytest
from tasks.task_88d import one_bounds, validate


@pytest.mark.parametrize("input, expected",
                         [(0, 2),(5, 7), (10, 21), (15, 26)],
                         ids=['for0', 'for5', 'for10', 'for15'
])
def test_one_bounds(input, expected):
    assert one_bounds(input) == expected

@pytest.mark.for_errors
def test_one_bounds_for_error():
    with pytest.raises(TypeError):
        one_bounds('qwerty')

@pytest.mark.for_errors
def test_one_bounds_for_error2():
    with pytest.raises(TypeError):
        one_bounds()

def test_validate():
    assert validate(12) == True

@pytest.mark.parametrize("input, expected",
                         [('qwerty', False),({}, False), ([], False)],
                         ids=['for_string', 'for_dict', 'for_list'
])
def test_validate_for_invalid(input, expected):
    assert validate(input) == expected
