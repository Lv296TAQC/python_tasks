import unittest
from tasks.task_569 import is_prime, prime_numbers, divide_by_prime, validate, natural_numbers


class TestTask(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(13), True)
        self.assertFalse(is_prime(21), False)
        self.assertFalse(is_prime(22), False)

    def test_prime_number(self):
        self.assertEquals(prime_numbers(32), [7, 11, 13, 17, 19, 23, 29, 31])

    def test_divide_by_prime(self):
        self.assertFalse(divide_by_prime(100), False)

    def test_validate(self):
        self.assertFalse(validate(100), False)

    def test_natural_numbers(self):
        self.assertEqual(natural_numbers(7), [30, 60, 90, 120, 150, 180, 240])
