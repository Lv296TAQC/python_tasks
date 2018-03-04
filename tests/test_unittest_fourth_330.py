import mock
import unittest
from tasks.fourth_330 import minus_last, ideal


class Test330(unittest.TestCase):

    @mock.patch('tasks.third_227')
    def test_third_330_minus_last(self, mock_path):
        mock_path.divisor.return_value = [1, -1, 2, -2, 3, -3, 6, -6]
        self.assertEqual(6, minus_last(6))

    def test_third_330_ideal(self):
        self.assertListEqual([6, 28, 496], ideal(501))


if __name__ == '__main__':
    unittest.main()