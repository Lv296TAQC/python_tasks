import unittest
from tasks.task_88a import task88a


class Test88a(unittest.TestCase):
    def test_asert_true_6(self):
        self.assertTrue(task88a(6))

    def test_asert_true_18(self):
        self.assertTrue(task88a(18))
    def test_asert_true_minus_18(self):
        self.assertTrue(task88a(-18))

    def test_asert_true_86(self):
        self.assertTrue(task88a(86))

    def test_assert_false_5(self):
        self.assertFalse(task88a(5))

    def test_assert_false_17(self):
        self.assertFalse(task88a(17))

    def test_assert_false_minus_17(self):
        self.assertFalse(task88a(-17))

    def test_assert_false_87(self):
        self.assertFalse(task88a(87))

    def test_raises_str(self):
        with self.assertRaises(TypeError):
            task88a('qweqw')

    def test_raises_float(self):
        with self.assertRaises(TypeError):
            task88a(10.5)
    def test_raises_list(self):
        with self.assertRaises(TypeError):
            task88a([10, 5])

    def test_raises_tuple(self):
        with self.assertRaises(TypeError):
            task88a((10, 5))

if __name__ == '__main__':
    unittest.main()
