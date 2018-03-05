""""Test for task1_88c"""

import unittest

from tasks.task_88c import swap_numb


class TestsTask88c(unittest.TestCase):
    """Test to check if the first and the last digits of the number are changing."""
    def test_swap_numb_first(self):
        """Check if expected results correspond to actual with a specific input"""
        res = swap_numb(1000)
        self.assertEqual(res, 1.0)
        res = swap_numb(5)
        self.assertEqual(res, 500e-2)
        res = swap_numb(939)
        self.assertEqual(res, 939.0000)
        res = swap_numb(731)
        self.assertEqual(res, 137)
        res = swap_numb(731)
        self.assertNotEqual(res, 137.0000000001)

    def test_swap_numb_second(self):
        """Test to check if input and output types of values correspond to
        intended, according to the function docstrings.
        """
        numb = 543
        res = swap_numb(numb)
        self.assertIsInstance(res, int)
        self.assertIsInstance(numb, int)

    def test_swap_numb_third(self):
        """Test to check if input and output types of values correspond to
        intended, according to the function docstrings.
        """
        self.assertRaises(TypeError, swap_numb, "aaa")
        self.assertRaises(TypeError, swap_numb, [])
        self.assertRaises(TypeError, swap_numb, (1,))
        self.assertRaises(ValueError, swap_numb, 0)
        self.assertRaises(ValueError, swap_numb, -100)


if __name__ == '__main__':
    unittest.main()
