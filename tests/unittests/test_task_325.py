import unittest
from task.task_325 import func4


class TestTask325(unittest.TestCase):

    def test_multiply_two_digits(self):
        number = 589
        expected = func4(number)
        self.assertEqual(expected, [19, 31])

    def test_with_zero(self):
        number = 0
        expected = func4(number)
        self.assertEqual(expected, [])

    def test_with_negative_number(self):
        number = -100
        expected = func4(number)
        self.assertEqual(expected, [])

    def test_sum_with_str(self):
        self.assertRaises(TypeError, func4, 'test_string')

    def test_with_list(self):
        self.assertRaises(TypeError, func4, [1])

    def test_with_tuple(self):
        self.assertRaises(TypeError, func4, (1,))

    def test_with_dict(self):
        self.assertRaises(TypeError, func4, {1: 2})



if __name__ == '__main__':
    unittest.main()
