""""Test for task4_331b"""

import unittest

from tasks.task_331b import func


class TestsTask331b(unittest.TestCase):
    """
        Test to check if all possible triples of natural numbers, which sum of squares
        is equal to the given natural number and satisfy x1 >= x2 >= x3, are found.
    """

    def test_func_first(self):
        """Check if expected results correspond to actual with a specific input"""
        int_ = 120
        res = func(int_)
        self.assertEqual(res, [(10, 4, 2)])

        int_ = 23
        res = func(int_)
        self.assertEqual(res, [])

        int_ = 3
        res = func(int_)
        self.assertEqual(res, [(1, 1, 1)])

        int_ = 90
        res = func(int_)
        self.assertEqual(res, [(7, 5, 4), (8, 5, 1), (9, 3, 0)])

    def test_func_second(self):
        """Test to check if input and output types of values corresponds to
        intended, according to the function docstrings.
        """
        integer = 100
        res = func(integer)
        self.assertIsInstance(integer, int)
        self.assertIsInstance(res, list)


if __name__ == '__main__':
    unittest.main()
