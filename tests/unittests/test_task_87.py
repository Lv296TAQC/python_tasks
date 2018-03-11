import unittest
from tasks.task_87 import natural_number


class TestTask87(unittest.TestCase):

    def test_normal_args(self):
        self.assertEqual(natural_number(1234, 2), 7)
        self.assertEqual(natural_number(7200, 2), 0)
        self.assertEqual(natural_number(1510, 0), 0)

    def test_greater_second_arg(self):
        self.assertEqual(natural_number(1, 4), 1)
        self.assertEqual(natural_number(815, 4), 14)

    def test_negative_args(self):
        self.assertRaises(ValueError, natural_number(-1234, 2))
        self.assertRaises(ValueError, natural_number(557, -1))
        self.assertRaises(ValueError, natural_number(5.57, 2))
        self.assertRaises(ValueError, natural_number(3967, 8.9))

    def test_str_arg(self):
        self.assertRaises(TypeError, natural_number('', 4))
        self.assertRaises(TypeError, natural_number('5dssa6578', 4))
        self.assertRaises(TypeError, natural_number(8569, ''))
        self.assertRaises(TypeError, natural_number(8569, '3'))


if __name__ == '__main__':
    unittest.main()
