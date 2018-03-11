import unittest
from tasks.task_226 import common_multiple


class TestTask226(unittest.TestCase):

    def test_normal_args(self):
        self.assertEqual(common_multiple(12, 22), [132])
        self.assertEqual(common_multiple(1, 1), [1])

    def test_negative_args(self):
        self.assertRaises(ValueError, common_multiple(-134, 2))
        self.assertRaises(ValueError, common_multiple(12, -1))

    def test_str_args(self):
        self.assertRaises(TypeError, common_multiple('', 4))
        self.assertRaises(TypeError, common_multiple('5dssa6578', 4))
        self.assertRaises(TypeError, common_multiple(8569, ''))
        self.assertRaises(TypeError, common_multiple(8569, '3'))


if __name__ == '__main__':
    unittest.main()
