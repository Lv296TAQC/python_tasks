import unittest
from task.task_225 import func3


class TestTask225(unittest.TestCase):

    def test_list_from_natural_number(self):
        number = 5000
        expected = func3(number)
        self.assertEqual(expected, [25, 50])

    def test_list_from_zero(self):
        number = 0
        expected = func3(number)
        self.assertEqual(expected, [])

    def test_with_str(self):
        self.assertRaises(TypeError, func3, 'test_string')

    def test_with_list(self):
        self.assertRaises(TypeError, func3, [1])

    def test_with_tuple(self):
        self.assertRaises(TypeError, func3, (1,))

    def test_with_dict(self):
        self.assertRaises(TypeError, func3, {1: 2})



if __name__ == '__main__':
    unittest.main()
