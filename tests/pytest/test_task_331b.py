""""Test for task4_331b"""

import pytest

from tasks.task_331b import func


class TestsTask331b(TestCase):
    """
        Test to check if all possible triples of natural numbers, which sum of squares
        is equal to the given natural number and satisfy x1 >= x2 >= x3, are found.
    """

    def test_func_first_a(self):
        """Check if expected results correspond to actual with a specific input"""
        int_ = 120
        res = func(int_)
        self.assertEqual(res, [(10, 4, 2)])

    def test_func_first_b(self):
        """Check if expected results correspond to actual with a specific input"""
        int_ = 23
        res = func(int_)
        self.assertEqual(res, [])

    def test_func_first_c(self):
        """Check if expected results correspond to actual with a specific input"""
        int_ = 3
        res = func(int_)
        self.assertEqual(res, [(1, 1, 1)])

    def test_func_first_d(self):
        """Check if expected results correspond to actual with a specific input"""
        int_ = 90
        res = func(int_)
        self.assertEqual(res, [(7, 5, 4), (8, 5, 1), (9, 3, 0)])

    def test_func_second_a(self):
        """Test to check if input and output types of values corresponds to
        intended, according to the function docstrings.
        """
        integer = 100
        func(integer)
        self.assertIsInstance(integer, int)

    def test_func_second_b(self):
        """Test to check if input and output types of values corresponds to
        intended, according to the function docstrings.
        """
        integer = 100
        res = func(integer)
        self.assertIsInstance(res, list)

    def test_func_third_a(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(TypeError, func, "Zero")

    def test_func_third_b(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(TypeError, func, [1, 2, 3])

    def test_func_third_c(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(TypeError, func, (1, 2, 0))

    def test_func_third_d(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(TypeError, func, -7e5)

    def test_func_third_e(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(ValueError, func, 0)

    def test_func_third_f(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(ValueError, func, -10)
