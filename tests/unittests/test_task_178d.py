import unittest
from tasks.task_178d import task_function


class TestCount(unittest.TestCase):

    def test_correct_value(self):
        self.assertEqual(task_function([15, 12, 19]), 1)

    def test_correct_value(self):
        self.assertEqual(task_function([15, 12, 19]), 0)

    def test_incorrect_value(self):
        self.assertEqual(task_function([1, 2, 3]), 0)

    def test_minus_value(self):
        self.assertEqual(task_function([-15, -12, -19]), 0)

    def test_minus_value(self):
        self.assertEqual(task_function([0, 0, 0]), 0)



if __name__ == '__main__':
    unittest.main()