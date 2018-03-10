import unittest
from tasks.task_331a import sum_of_three_squares


class TestTask331(unittest.TestCase):

    def test_correct_value(self):
        self.assertEqual(sum_of_three_squares(12), (2, 2, 2))

    def test_incorrect_value(self):
        self.assertEqual(sum_of_three_squares(5), (2, 2, 2))

    def test_zero_value(self):
        self.assertEqual(sum_of_three_squares(0), (0, 0, 0))

    def test_raises_str(self):
        with self.assertRaises(TypeError):
              tasks.task_331a('error')

if __name__ == '__main__':
    unittest.main()