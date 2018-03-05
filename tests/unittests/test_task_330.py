import unittest
from unittest.mock import patch
from tasks.task_330 import minus_last, ideal


class TestsTask330(unittest.TestCase):

    @patch('tasks.task_227.divisor', return_value=[1, -1, 2, -2, 3, -3, 6, -6])
    def test_third_330_minus_last(self, divisor):
        self.assertEqual(6, minus_last(6))

    def test_third_330_ideal(self):
        self.assertListEqual([6, 28, 496], ideal(501))


if __name__ == '__main__':
    unittest.main()