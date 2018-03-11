import unittest
from tasks.task_329 import sum_of_digits, main_func


class TestTask329(unittest.TestCase):

    def test_sum_of_digits_normal_arg(self):
        self.assertEqual(sum_of_digits(15), 6)
        self.assertEqual(sum_of_digits(1), 1)

    def test_sum_of_digits_negative_arg(self):
        self.assertEqual(sum_of_digits(-1), -1)

    def test_sum_of_digits_str_arg(self):
        self.assertRaises(TypeError, sum_of_digits('5'))

    def test_main_func_normal_args(self):
        self.assertEqual(main_func(24, 36), [6, 15])

    def test_main_func_negative_args(self):
        self.assertRaises(ValueError, main_func(-100, 36))

    def test_main_func_str_arg(self):
        self.assertRaises(TypeError, main_func('21', 25))
        self.assertRaises(TypeError, main_func(21, '25'))
        self.assertRaises(TypeError, main_func('21', '25'))


if __name__ == '__main__':
    unittest.main()
