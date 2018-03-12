import unittest
from tasks.task_88d import one_bounds, validate


class TestsTask88d(unittest.TestCase):

    def test_one_bounds(self):
        for i in range(0, 20, 5):
            with self.subTest():
                self.assertIn(one_bounds(i), [2, 7, 21, 26])

    def test_one_bounds_for_errors(self):
        self.assertRaises((TypeError, ValueError), one_bounds, -2, 13.5, 'qwerty', [1], False)

    def test_validate(self):
        self.assertTrue(validate(12))

    def test_validate_for_invalid(self):
        for i in ('qwerty', {}, []):
            with self.subTest():
                self.assertFalse(validate(i))
