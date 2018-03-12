""""Test for task4_331b"""

import pytest

from tasks.task_331b import func


def test_func_first_a():
    """Check if expected results correspond to actual with a specific input"""
    int_ = 120
    res = func(int_)
    assert res == [(10, 4, 2)]


def test_func_first_b():
    """Check if expected results correspond to actual with a specific input"""
    int_ = 23
    res = func(int_)
    assert res == []


def test_func_first_c():
    """Check if expected results correspond to actual with a specific input"""
    int_ = 3
    res = func(int_)
    assert res == [(1, 1, 1)]


def test_func_first_d():
    """Check if expected results correspond to actual with a specific input"""
    int_ = 90
    res = func(int_)
    assert res == [(7, 5, 4), (8, 5, 1), (9, 3, 0)]


def test_func_second_a():
    """Test to check if input and output types of values corresponds to
    intended, according to the function docstrings.
    """
    assert type(func(110)) == int
    assert isinstance(func(110), int)
    numb = 110
    assert type(numb) == int
    assert isinstance(func(numb), int)


def test_func_third_a():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(TypeError):
        func("Zero")


def test_func_third_b():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(TypeError):
        func([1, 2, 3])


def test_func_third_c():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(TypeError):
        func((1, 2, 0))


def test_func_third_d():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(TypeError):
        func(-7e5)


def test_func_third_e():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(ValueError):
        func(0)


def test_func_third_f():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(ValueError):
        func(-10)
