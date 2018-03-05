""""Test for task1_88c"""

from unittest import TestCase

from tasks.task_88c import swap_numb


class TestsTask88c(TestCase):
    """Test to check if the first and the last digits of the number are changing."""
    def test_swap_numb_first_a(self):
        """Check if expected results correspond to actual with a specific input"""
        res = swap_numb(1000)
        self.assertEqual(res, 1.0)

    def test_swap_numb_first_b(self):
        """Check if expected results correspond to actual with a specific input"""
        res = swap_numb(5)
        self.assertEqual(res, 500e-2)

    def test_swap_numb_first_c(self):
        """Check if expected results correspond to actual with a specific input"""
        res = swap_numb(939)
        self.assertEqual(res, 939.0000)

    def test_swap_numb_first_d(self):
        """Check if expected results correspond to actual with a specific input"""
        res = swap_numb(731)
        self.assertEqual(res, 137)

    def test_swap_numb_first_e(self):
        """Check if expected results correspond to actual with a specific input"""
        res = swap_numb(731)
        self.assertNotEqual(res, 137.0000000001)

    def test_swap_numb_second_a(self):
        """Test to check if input and output types of values correspond to
        intended, according to the function docstrings.
        """
        numb = 543
        res = swap_numb(numb)
        self.assertIsInstance(res, int)

    def test_swap_numb_second_b(self):
        """Test to check if input and output types of values correspond to
        intended, according to the function docstrings.
        """
        numb = 543
        swap_numb(numb)
        self.assertIsInstance(numb, int)

    def test_swap_numb_third_a(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(TypeError, swap_numb, "aaa")

    def test_swap_numb_third_b(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(TypeError, swap_numb, [])

    def test_swap_numb_third_c(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(TypeError, swap_numb, (1,))

    def test_swap_numb_third_d(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(ValueError, swap_numb, 0)

    def test_swap_numb_third_e(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(ValueError, swap_numb, -100)
