import unittest
from tasks.task_559 import is_prime_number, return_prime_number, number_of_mercenn


class TestTask559(unittest.TestCase):

    def test_is_5_prime_number(self):
        self.assertTrue(is_prime_number(5))

    def test_is_10_not_prime_number(self):
        self.assertFalse(is_prime_number(10))

    def test_is_prime_number_negative_arg(self):
        self.assertRaises(ValueError, is_prime_number(-7))

    def test_is_prime_number_str_arg(self):
        self.assertRaises(TypeError, is_prime_number('25'))
        self.assertRaises(TypeError, is_prime_number('hhg'))

    def test_return_prime_number_normal_arg(self):
        self.assertEqual(return_prime_number(6), [1, 2, 3, 5])

    def test_return_prime_number_negative_arg(self):
        self.assertRaises(ValueError, return_prime_number(-12))

    def test_return_prime_number_str_arg(self):
        self.assertRaises(TypeError, return_prime_number('6'))
        self.assertRaises(TypeError, return_prime_number('2#6'))

    def test_number_of_mercenn_normal_arg(self):
        self.assertEqual(return_prime_number(10), [3, 7])

    def test_number_of_mercenn_negative_arg(self):
        self.assertRaises(ValueError, return_prime_number(-142))

    def test_number_of_mercenn_str_arg(self):
        self.assertRaises(TypeError, return_prime_number('788'))
        self.assertRaises(TypeError, return_prime_number('sd8'))


if __name__ == '__main__':
    unittest.main()
