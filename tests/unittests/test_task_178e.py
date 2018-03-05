""""Test for task2_178e"""

import unittest

from tasks.task_178e import func


class TestsTask88c(unittest.TestCase):
    """Test to check if the right count of the elements satisfying the condition:
    (2^k < ak < k!) for k in range(1, n), e.g. a1, a2, a3, ... , an
    """

    def test_func_first(self):
        """Check if expected results correspond to actual with a specific input"""
        list_ = [3, 5, 12, 15, 23, 34, 56]
        res = func(list_)
        self.assertEqual(res, 0)

        list_ = [0, 0, 0, 0, 0, 0, 0]
        res = func(list_)
        self.assertEqual(res, 0)

        list_ = [5]
        res = func(list_)
        self.assertEqual(res, 0)

        list_ = [1, 2, 3, 4, 5, 122]
        res = func(list_)
        self.assertEqual(res, 1)

        list_ = [1, 2, 3, 4, 5, 6, 7, 260, 540, 100500]
        res = func(list_)
        self.assertEqual(res, 3)

    def test_func_second(self):
        """Test to check if input and output types of values correspond to
        intended, according to the function docstrings.
        """
        list_ = [3, 5, 12, 15, 23, 34, 56]
        res = func(list_)
        self.assertIsInstance(list_, list)
        self.assertIsInstance(res, int)


if __name__ == '__main__':
    unittest.main()
