import unittest
from tasks.task_243a import sum_of_two_squares


class TestsTask243(unittest.TestCase):
    def test_correct_value(self):
        self.assertEqual(sum_of_two_squares(8), (2, 2))

if __name__ == '__main__':
    unittest.main()