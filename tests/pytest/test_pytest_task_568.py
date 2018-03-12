import pytest
from tasks.task_568 import find_subset, single_solution


@pytest.mark.parametrize("input, expected",
                         [(-10, -35), (-5, -33), (0, 123456789), (5, 3456788)
])
def test_find_subset(input, expected):
    assert find_subset(input) == expected

@pytest.mark.for_errors
def test_find_subset_for_errors():
    with pytest.raises(TypeError):
        find_subset('qwerty')

@pytest.mark.for_errors
def test_find_subset_for_errors():
    with pytest.raises(TypeError):
        find_subset([])

@pytest.mark.parametrize("input, expected",
                         [(123, '1+23+4+5-6+7+89'), (57, '1+2-3-45+6+7+89'), (1, '1+23-45-67+89')
])
def test_single_solution(input, expected):
    assert single_solution(input) == expected

@pytest.mark.parametrize("input, expected",
                         [('qwerty', 'Invalid input. Please write correct natural number'), (123456, 'No possible solutions')
])
def test_single_solution_for_invalid(input, expected):
    assert single_solution(input) == expected
