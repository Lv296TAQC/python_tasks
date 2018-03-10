import unittest
from tasks.task_88b import reverse_int


class TestReverseInt(unittest.TestCase):

    def test_incorrect_value(self):
        self.assertEqual(reverse_int(15), 50)

    def test_correct_value(self):
        self.assertEqual(reverse_int(15), 51)

    def test_zero_value(self):
        self.assertEqual(reverse_int(0), 0)

    def test_minus_value(self):
        self.assertEqual(reverse_int(-23), -32)

    def test_fractional_value(self):
        self.assertEqual(reverse_int(2.3), 3.2)


if __name__ == '__main__':
    unittest.main()
