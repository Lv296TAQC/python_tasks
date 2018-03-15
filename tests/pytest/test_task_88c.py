""""Test for task1_88c"""

import pytest

from tasks.task_88c import swap_numb


def test_swap_numb_first_a():
    """Check if expected results correspond to actual with a specific input"""
    assert swap_numb(1000) == 1.0


def test_swap_numb_first_b():
    """Check if expected results correspond to actual with a specific input"""
    assert swap_numb(5) == 500e-2


def test_swap_numb_first_c():
    """Check if expected results correspond to actual with a specific input"""
    assert swap_numb(939) == 939.0000


def test_swap_numb_first_d():
    """Check if expected results correspond to actual with a specific input"""
    assert swap_numb(731) == 137


def test_swap_numb_first_e():
    """Check if expected results correspond to actual with a specific input"""
    assert swap_numb(731) != 137.0000000001


def test_swap_numb_second_a():
    """Test to check if input and output types of values correspond to
    intended, according to the function docstrings.
    """
    assert 543 .__class__ is int
    assert isinstance(swap_numb(543), int)
    numb = 543
    assert type(numb) == int
    assert isinstance(swap_numb(numb), int)


def test_swap_numb_third_a():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(TypeError):
        swap_numb("aaa")


def test_swap_numb_third_b():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(TypeError):
        swap_numb([])


def test_swap_numb_third_c():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(TypeError):
        swap_numb((1,))


def test_swap_numb_third_d():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(ValueError):
        swap_numb(0)


def test_swap_numb_third_e():
    """Test to check if expected Error raises when input is not valid"""
    with pytest.raises(ValueError):
        swap_numb(-100)
