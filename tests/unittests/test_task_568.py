import unittest
from task_568 import find_subset, single_solution
from tasks.task_88d import validate


class TestsTask568(unittest.TestCase):

    def test_find_subset(self):
        for i in range(-10, 30, 5):
            with self.subTest():
                self.assertIn(find_subset(i), [-35, -33, 123456789, 3456788, 456813, 456798, -456811, -456789])

    def test_find_subset_for_errors(self):
        self.assertRaises((TypeError, ValueError), find_subset, 'qwerty', [1], {1:2})

    def test_single_solution(self):
        for i in range(3):
            with self.subTest():
                self.assertEqual(single_solution(123), '1+23+4+5-6+7+89')
                self.assertEqual(single_solution(57), '1+2-3-45+6+7+89')
                self.assertEqual(single_solution(1), '1+23-45-67+89')

    def test_single_solution_for_invalid(self):
        for i in range(3):
            with self.subTest():
                self.assertEqual(single_solution('qwerty'), 'Invalid input. Please write correct natural number')
                self.assertEqual(single_solution(-794), 'Invalid input. Please write correct natural number')
                self.assertEqual(single_solution(123456), 'No possible solutions')


if __name__ == '__main__':
    unittest.main()