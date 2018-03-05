import unittest
from unittest.mock import patch
from tasks.task_330 import minus_last, ideal


class TestsTask330(unittest.TestCase):

    @patch('tasks.task_227.divisor', return_value=[1, -1, 2, -2, 3, -3, 6, -6])
    def test_third_330_minus_last(self, divisor):
        self.assertEqual(6, minus_last(6))
        self.assertRaises(TypeError, minus_last, 'opa4a')
        self.assertRaises(TypeError, minus_last, [4])
        self.assertRaises(TypeError, minus_last, {8: 3})
        self.assertRaises(TypeError, minus_last, {8, 3})
        self.assertRaises(TypeError, minus_last, False)  # Should give us TypeError(Ask)

    def test_third_330_ideal(self):
        self.assertListEqual([6, 28, 496], ideal(501))
        self.assertRaises(TypeError, ideal, 'opa4a')
        self.assertRaises(TypeError, ideal, (8, 3))
        self.assertRaises(TypeError, ideal, [4])
        self.assertRaises(TypeError, ideal, {8: 3})
        self.assertRaises(TypeError, ideal, {8, 3})
        self.assertRaises(TypeError, ideal, False)  # Should give us TypeError(Ask)


if __name__ == '__main__':
    unittest.main()
