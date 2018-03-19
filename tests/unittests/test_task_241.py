import unittest
from tasks.task_241 import difficult_formula, validate_values


class TestsTask241(unittest.TestCase):

    def test_difficult_formula(self):
        self.assertEqual(difficult_formula(44, 2.5), -3076222890240854.5+1.1630684374642796e+16j)

    def test_difficult_formula_for_errors(self):
        self.assertRaises((TypeError, ValueError), difficult_formula, 'qwerty', False)

    def test_validate_values(self):
        self.assertTrue(validate_values(32, 34.5))
        self.assertFalse(validate_values(-32, 'qwerty'))

    def test_validate_values_for_errors(self):
        self.assertRaises(TypeError, validate_values)
        self.assertRaises(TypeError, validate_values, 1)