import unittest
from tasks.task_182 import sum_div5_notdiv7


class TestsTask182(unittest.TestCase):

    def test_sum_div5_notdiv7(self):
        self.assertSequenceEqual(sum_div5_notdiv7([5, 10, 107, 456]), (15, 2))

    def test_sum_div5_notdiv7_errors(self):
        self.assertRaises((TypeError, ValueError), sum_div5_notdiv7, 54, 'qwerty', False, {1:2})
