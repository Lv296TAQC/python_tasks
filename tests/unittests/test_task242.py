import unittest
from tasks.task_242 import total_sum


class TestTask242(unittest.TestCase):
    def test_total_positive_value_1(self):
        self.assertEquals(total_sum(1), 2.0)

    def test_total_positive_value_4(self):
        self.assertEquals(total_sum(4), 1.375)

    def test_total_positive_value_7(self):
        self.assertEquals(total_sum(7), 1.3817460317460317)

    def test_total_positive_value_10(self):
        self.assertEquals(total_sum(10), 1.3817733134920636)

    def test_total_negative_value(self):
        self.assertEquals(total_sum(-1), 0)

    def test_total_raise_str(self):
        with self.assertRaises(TypeError):
            total_sum('asas')
