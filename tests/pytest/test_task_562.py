""""Test for task5_562"""

import pytest
from unittest.mock import patch

from tasks.task_562 import split_into_digits, get_armstrong_numbs


def test_split_into_digits_first_a():
    """Check if expected results correspond to actual with a specific input"""
    int_ = 120
    res = split_into_digits(int_)
    assert res == [1, 2, 0]


def test_split_into_digits_first_b():
    """Check if expected results correspond to actual with a specific input"""
    int_ = 1
    res = split_into_digits(int_)
    assert res == [1]


def test_split_into_digits_first_c():
    """Check if expected results correspond to actual with a specific input"""
    int_ = 9876543210
    res = split_into_digits(int_)
    assert res == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def test_split_into_digits_second_a():
    """Test to check if input and output types of values correspond to
    intended, according to the function docstrings.
    """
    int_ = 95
    assert type(split_into_digits(int_)) == list
    assert isinstance(split_into_digits(int_), list)


def test_split_into_digits_third_a():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(TypeError):
        split_into_digits("kal-el")


def test_split_into_digits_third_b():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(ValueError):
        split_into_digits(-1000)


def test_get_armstrong_first_a():
    """Check if expected results correspond to actual with a specific input"""
    left = 22
    right = 4444
    res = get_armstrong_numbs(left, right)
    assert res == [153, 370, 371, 407, 1634]


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
    assert type(left) == int
    assert isinstance(left, int)
    assert type(right) == int
    assert isinstance(right, int)
    assert type(res) == list
    assert isinstance(res, list)


def test_get_armstrong_third_a():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(TypeError):
        get_armstrong_numbs("joer-el", "cryot")


def test_get_armstrong_third_b():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(ValueError):
        get_armstrong_numbs(-1000, 1000)
