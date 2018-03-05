""""Test for task3_243b"""

from unittest import TestCase

from tasks.task_243b import func


class TestsTask243b(TestCase):
    """
        Test to check if all possible pairs of natural numbers, which sum of squares
        is equal to the given natural number and satisfy x1 >= x2, are found.
    """

    def test_func_first(self):
        """Check if expected results correspond to actual with a specific input"""
        int_ = 80
        res = func(int_)
        self.assertEqual(res, [(8, 4)])

        int_ = 99
        res = func(int_)
        self.assertEqual(res, [])

        int_ = 2
        res = func(int_)
        self.assertEqual(res, [(1, 1)])

        int_ = 725
        res = func(int_)
        self.assertEqual(res, [(23, 14), (25, 10), (26, 7)])

    def test_func_second(self):
        """Test to check if input and output types of values corresponds to
        intended, according to the function docstrings.
        """
        int_ = 50
        res = func(int_)
        self.assertIsInstance(int_, int)
        self.assertIsInstance(res, list)

    def test_swap_numb_third_a(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(TypeError, func, "1e1")

    def test_swap_numb_third_b(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(TypeError, func, [complex(1, 2)])

    def test_swap_numb_third_c(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(TypeError, func, (0, 0, 0))

    def test_swap_numb_third_d(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(ValueError, func, 0)

    def test_swap_numb_third_e(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(ValueError, func, -1)
