import unittest
from tasks.task_332 import lagrange


class TestsTask332(unittest.TestCase):

    def test_lagrange(self):
        self.assertEqual(lagrange(123), (11, 1, 1, 0))

    def test_lagrange_for_errors(self):
        self.assertRaises((TypeError, ValueError), lagrange, 'qwerty', -123, False, [1])
