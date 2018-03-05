import unittest
from tasks.task_88d import one_bounds, validate


class TestsTask88d(unittest.TestCase):

    @unittest.expectedFailure
    def test_one_bounds(self):
        for i in range(0, 20, 5):
            with self.subTest():
                self.assertIn(one_bounds(i), [101, 151, 1101, 1151])

    def test_one_bounds_for_errors(self):
            self.assertRaises((TypeError, ValueError), one_bounds, -2, 13.5, 'qwerty', [1], False)

    def test_validate(self):
        self.assertTrue(validate(12))

    def test_validate_for_invalid(self):
        for i in range(3):
            with self.subTest():
                self.assertFalse(validate('qwerty'))
                self.assertFalse(validate({}))
                self.assertFalse(validate([]))


if __name__ == '__main__':
    unittest.main()