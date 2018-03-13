import unittest
from task.task_108 import func2


class TestTask108(unittest.TestCase):

    def test_with_natural_number(self):
        number = 5
        expected = func2(number)
        self.assertEqual(expected, 8)

    def test_with_zero(self):
        number = 0
        expected = func2(number)
        self.assertEqual(expected, 2)

    def test_with_str(self):
        self.assertRaises(TypeError, func2, 'test_string')

    def test_with_list(self):
        self.assertRaises(TypeError, func2, [1])

    def test_with_tuple(self):
        self.assertRaises(TypeError, func2, (1,))

    def test_with_dict(self):
        self.assertRaises(TypeError, func2, {1: 2})



if __name__ == '__main__':
    unittest.main()
