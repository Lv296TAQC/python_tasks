from tasks.task_86g import total_sum1
import unittest


class TestTask86g(unittest.TestCase):
    def test_value_22222(self):
        self.assertTrue(total_sum1(22222), 2)

    def test_value_12345(self):
        self.assertTrue(total_sum1(12345), 3)

    def test_value_54321(self):
        self.assertTrue(total_sum1(54321), 3)

    def test_raises_float(self):
        with self.assertRaises(ValueError):
            total_sum1(10.5)

    def test_raises_negative_value(self):
        with self.assertRaises(ValueError):
            total_sum1(-1)

    def test_raises_str(self):
        with self.assertRaises(ValueError):
            total_sum1("asd")

    def test_raises_list(self):
        with self.assertRaises(ValueError):
            total_sum1([123, 23, 12])
