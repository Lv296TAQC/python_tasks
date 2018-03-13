import unittest
from tasks.task_555 import triagle


class TestTask555(unittest.TestCase):

    def test_with_correct_value(self):
        number = 2
        expected = triagle(number)
        self.assertEqual(expected, [[1], [1, 1]])

    def test_with_zero(self):
        number = 0
        expected = triagle(number)
        self.assertEqual(expected, [])

    def test_with_negative_number(self):
        number = -100
        expected = triagle(number)
        self.assertEqual(expected, [])

    def test_with_str(self):
        self.assertRaises(TypeError, triagle, 'test_string')

    def test_with_list(self):
        self.assertRaises(TypeError, triagle, [1])

    def test_with_tuple(self):
        self.assertRaises(TypeError, triagle, (1,))

    def test_with_dict(self):
        self.assertRaises(TypeError, triagle, {1: 2})

    def test_with_float(self):
        self.assertRaises(TypeError, triagle, 5.5)


if __name__ == '__main__':
    unittest.main()
