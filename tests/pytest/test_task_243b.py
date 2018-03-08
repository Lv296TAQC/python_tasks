""""Test for task3_243b"""

import pytest

from tasks.task_243b import func


def test_func_first_a():
    """Check if expected results correspond to actual with a specific input"""
    int_ = 80
    res = func(int_)
    assert res, [(8, 4)]


def test_func_first_b():
    """Check if expected results correspond to actual with a specific input"""
    int_ = 99
    res = func(int_)
    assert res, []


def test_func_first_c():
    """Check if expected results correspond to actual with a specific input"""
    int_ = 2
    res = func(int_)
    assert res, [(1, 1)]


def test_func_first_d():
    """Check if expected results correspond to actual with a specific input"""
    int_ = 725
    res = func(int_)
    assert res, [(23, 14), (25, 10), (26, 7)]


def test_func_second_a():
    """Test to check if input and output types of values corresponds to
    intended, according to the function docstrings.
    """
    int_ = 50
    func(int_)
    assertIsInstance(int_, int)


def test_func_second_b():
    """Test to check if input and output types of values corresponds to
    intended, according to the function docstrings.
    """
    int_ = 50
    res = func(int_)
    assertIsInstance(res, list)


def test_func_third_a():
    """Test to check if expected Error raises when input is not valid"""
    assertRaises(TypeError, func, "1e1")


def test_func_third_b():
    """Test to check if expected Error raises when input is not valid"""
    assertRaises(TypeError, func, [complex(1, 2)])


def test_func_third_c():
    """Test to check if expected Error raises when input is not valid"""
    assertRaises(TypeError, func, (0, 0, 0))


def test_func_third_d():
    """Test to check if expected Error raises when input is not valid"""
    assertRaises(ValueError, func, 0)


def test_func_third_e():
    """Test to check if expected Error raises when input is not valid"""
    assertRaises(ValueError, func, -1)
