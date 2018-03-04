import unittest
from tasks.third_227 import (comparison,
                             divisor)


class Test227(unittest.TestCase):

    def test_third_227_comparison(self):
        self.assertListEqual({1, -1, 2, -2, 3, -3, 6, -6}, comparison(18, 6))

    def test_third_227_divisor(self):
        self.assertListEqual({1, -1, 2, -2, 3, -3, 6, -6}, divisor(6))


if __name__ == '__main__':
    unittest.main()
