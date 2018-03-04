import unittest
from tasks.moo224 import task224


class Test224(unittest.TestCase):
    def test_task224(self):
        self.assertListEqual([1, 2, 3, 6], task224(6))
        self.assertListEqual([1, 2, 4, 8], task224(8))
        self.assertListEqual([], task224(0))
        self.assertListEqual([1, 2, 3, 6, 7, 14, 21, 42], task224(42))
        self.assertListEqual([1, 3, 9, 27, 81], task224(81))


if __name__ == '__main__':
    unittest.main()
