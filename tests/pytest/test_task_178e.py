""""Test for task2_178e"""

import pytest

from tasks.task_178e import func


def test_func_first_a():
    """Check if expected results correspond to actual with a specific input"""
    list_ = [3, 5, 12, 15, 23, 34, 56]
    assert func(list_) == 0


def test_func_first_b():
    """Check if expected results correspond to actual with a specific input"""
    list_ = [0, 0, 0, 0, 0, 0, 0]
    assert func(list_) == 0


def test_func_first_c():
    """Check if expected results correspond to actual with a specific input"""
    list_ = [5]
    assert func(list_) == 0


def test_func_first_d():
    """Check if expected results correspond to actual with a specific input"""
    list_ = [1, 2, 3, 4, 5, 122]
    assert func(list_) == 1


def test_func_first_e():
    """Check if expected results correspond to actual with a specific input"""
    list_ = [1, 2, 3, 4, 5, 6, 7, 260, 540, 100500]
    assert func(list_) == 3


def test_func_second_a():
    """Test to check if input and output types of values correspond to
    intended, according to the function docstrings.
    """
    list_ = [3, 5, 12, 15, 23, 34, 56]
    func(list_)
    assert type(list_) == list
    assert isinstance(list_, list)
    assert type(func(list_)) == int
    assert isinstance(func(list_), int)


def test_swap_numb_third_a():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(TypeError):
        func({})


def test_swap_numb_third_b():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(ValueError):
        func(-1000)


def test_swap_numb_third_c():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(TypeError):
        func(("", ""))


def test_swap_numb_third_d():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(TypeError):
        func(["a", "b"])


def test_swap_numb_third_e():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(TypeError):
        func([0, -19])
