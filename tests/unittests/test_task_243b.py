""""Test for task3_243b"""

import unittest

from tasks.task_243b import func


class TestsTask243b(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
