import unittest
from tasks.task_227 import comparison, divisor


class TestsTask227(unittest.TestCase):

    def test_third_227_comparison(self):
        self.assertListEqual([-6, -3, -2, -1, 1, 2, 3, 6], comparison(18, 6))
        self.assertRaises(TypeError, comparison, 'abc', 2)
        self.assertRaises(TypeError, comparison, 3, {})
        self.assertRaises(TypeError, comparison, 1)
        self.assertRaises(TypeError, comparison)
        self.assertRaises(TypeError, comparison, 5, [])

    def test_third_227_divisor(self):
        self.assertListEqual([1, 2, 3, 6], divisor(6))
        self.assertRaises(TypeError, divisor, 'opa4a')
        self.assertRaises(TypeError, divisor)
        self.assertRaises(TypeError, divisor, [4])
        self.assertRaises(TypeError, divisor, {8, 4})
        self.assertRaises(TypeError, divisor, (1, 5))
