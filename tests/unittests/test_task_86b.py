import unittest
from tasks.task_86b import sum_of_digits


class TestTask86b(unittest.TestCase):

    def test_sum_of_digits(self):
        number = 34
        expected = sum_of_digits(number)
        self.assertEqual(expected, 7)

    def test_sum_with_zeroes_and_one(self):
        number = 1000
        expected = sum_of_digits(number)
        self.assertEqual(expected, 1)

    def test_sum_with_zero(self):
        number = 0
        expected = sum_of_digits(number)
        self.assertEqual(expected, 0)

    def test_sum_with_minus_one(self):
        self.assertRaises(ValueError, sum_of_digits, -1)

    def test_with_str(self):
        self.assertRaises(ValueError, sum_of_digits, 'test_string')

    def test_with_list(self):
        self.assertRaises(ValueError, sum_of_digits, [1])

    def test_with_tuple(self):
        self.assertRaises(ValueError, sum_of_digits, (1,))

    def test_with_dict(self):
        self.assertRaises(ValueError, sum_of_digits, {1: 2})

    def test_with_float(self):
        self.assertRaises(ValueError, sum_of_digits, 5.5)


if __name__ == '__main__':
    unittest.main()
