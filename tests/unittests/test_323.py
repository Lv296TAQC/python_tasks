import unittest
from tasks.moo323 import task323


class Test323(unittest.TestCase):
    def test_task323(self):
        self.assertListEqual([1], task323(2))
        self.assertListEqual([1, 5], task323(6))
        self.assertListEqual([1, 3, 5, 7], task323(8))
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                              26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], task323(41))
        self.assertListEqual([1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39], task323(40))
