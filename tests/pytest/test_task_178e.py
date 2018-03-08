""""Test for task2_178e"""

import pytest

from tasks.task_178e import func


class TestsTask88c(TestCase):
    """Test to check if the right count of the elements satisfying the condition:
    (2^k < ak < k!) for k in range(1, n), e.g. a1, a2, a3, ... , an
    """

    def test_func_first_a(self):
        """Check if expected results correspond to actual with a specific input"""
        list_ = [3, 5, 12, 15, 23, 34, 56]
        res = func(list_)
        self.assertEqual(res, 0)

    def test_func_first_b(self):
        """Check if expected results correspond to actual with a specific input"""
        list_ = [0, 0, 0, 0, 0, 0, 0]
        res = func(list_)
        self.assertEqual(res, 0)

    def test_func_first_c(self):
        """Check if expected results correspond to actual with a specific input"""
        list_ = [5]
        res = func(list_)
        self.assertEqual(res, 0)

    def test_func_first_d(self):
        """Check if expected results correspond to actual with a specific input"""
        list_ = [1, 2, 3, 4, 5, 122]
        res = func(list_)
        self.assertEqual(res, 1)

    def test_func_first_e(self):
        """Check if expected results correspond to actual with a specific input"""
        list_ = [1, 2, 3, 4, 5, 6, 7, 260, 540, 100500]
        res = func(list_)
        self.assertEqual(res, 3)

    def test_func_second_a(self):
        """Test to check if input and output types of values correspond to
        intended, according to the function docstrings.
        """
        list_ = [3, 5, 12, 15, 23, 34, 56]
        func(list_)
        self.assertIsInstance(list_, list)

    def test_func_second_b(self):
        """Test to check if input and output types of values correspond to
        intended, according to the function docstrings.
        """
        list_ = [3, 5, 12, 15, 23, 34, 56]
        res = func(list_)
        self.assertIsInstance(res, int)

    def test_swap_numb_third_a(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(ValueError, func, dict())

    def test_swap_numb_third_b(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(ValueError, func, -1000)

    def test_swap_numb_third_c(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(TypeError, func, ("", ""))

    def test_swap_numb_third_d(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(ValueError, func, ["a", "b"])

    def test_swap_numb_third_e(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(ValueError, func, [0, -19])
