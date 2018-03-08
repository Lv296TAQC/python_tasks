""""Test for task5_562"""

import pytest

from tasks.task_562 import split_into_digits, get_armstrong_numbs


def test_split_into_digits_first_a():
    """Check if expected results correspond to actual with a specific input"""
    int_ = 120
    res = split_into_digits(int_)
    assert res, [1, 2, 0]


def test_split_into_digits_first_b():
    """Check if expected results correspond to actual with a specific input"""
    int_ = 1
    res = split_into_digits(int_)
    assert res, [1]


def test_split_into_digits_first_c():
    """Check if expected results correspond to actual with a specific input"""
    int_ = 9876543210
    res = split_into_digits(int_)
    assert res, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def test_split_into_digits_second_a():
    """Test to check if input and output types of values correspond to
    intended, according to the function docstrings.
    """
    int_ = 100
    split_into_digits(int_)
    assertIsInstance(int_, int)


def test_split_into_digits_second_b():
    """Test to check if input and output types of values correspond to
    intended, according to the function docstrings.
    """
    int_ = 100
    res = split_into_digits(int_)
    assertIsInstance(res, list)


def test_split_into_digits_third_a():
    """Test to check if expected Error raises when input is not valid"""
    assertRaises(TypeError, split_into_digits, "kal-el")


def test_split_into_digits_third_b():
    """Test to check if expected Error raises when input is not valid"""
    assertRaises(ValueError, split_into_digits, -1000)


def test_get_armstrong_first_a():
    """Check if expected results correspond to actual with a specific input"""
    left = 22
    right = 4444
    res = get_armstrong_numbs(left, right)
    assert res, [153, 370, 371, 407, 1634]


def test_get_armstrong_first_b():
    """Check if expected results correspond to actual with a specific input"""
    left = 10
    right = 9999
    res = get_armstrong_numbs(left, right)
    assert res == [153, 370, 371, 407, 1634, 8208, 9474]
    assert len(res) == 7


def test_get_armstrong_second_a():
    """Test to check if input and output types of values correspond to
    intended, according to the function docstrings.
    """
    left = 99
    right = 1000
    res = get_armstrong_numbs(left, right)
    assertIsInstance(left, int)
    assertIsInstance(right, int)
    assertIsInstance(res, list)


def test_get_armstrong_second_b():
    """Test to check if input and output types of values correspond to
    intended, according to the function docstrings.
    """
    left = 99
    right = 1000
    res = get_armstrong_numbs(left, right)
    assertIsInstance(res, list)


def test_get_armstrong_third_a():
    """Test to check if expected Error raises when input is not valid"""
    assertRaises(TypeError, get_armstrong_numbs, "joer-el", "cryot")


def test_get_armstrong_third_b():
    """Test to check if expected Error raises when input is not valid"""
    assertRaises(ValueError, get_armstrong_numbs, -1000, 1000)


@patch('tasks.task_562.split_into_digits', return_value=[4, 0, 7])
def test_get_armstrong_fourth(, split_into_digits):  # pylint: disable=W0621
    """Check if expected results correspond to actual with a specific input, which isn't
    intended to change result hence mocked function split_into_digits"""
    left = 10
    right = 9999
    res = get_armstrong_numbs(left, right)
    assert split_into_digits(407) == [4, 0, 7]
    assert res == [407]
