import unittest
from tasks.task_224 import task224


class Test224(unittest.TestCase):
    def test_task224_6(self):
        self.assertListEqual([1, 2, 3, 6], task224(6))

    def test_task224_minus_6(self):
        self.assertListEqual([], task224(-6))

    def test_task224_zero(self):
        self.assertListEqual([], task224(0))

    def test_task224_8(self):
        self.assertListEqual([1, 2, 4, 8], task224(8))

    def test_task224_0(self):
        self.assertListEqual([], task224(0))

    def test_task224_42(self):
        self.assertListEqual([1, 2, 3, 6, 7, 14, 21, 42], task224(42))

    def test_task224_81(self):
        self.assertListEqual([1, 3, 9, 27, 81], task224(81))

    def test_raises_str(self):
        with self.assertRaises(TypeError):
            task224('qweqw')

    def test_raises_float(self):
        with self.assertRaises(TypeError):
            task224(10.5)
    def test_raises_list(self):
        with self.assertRaises(TypeError):
            task224([10, 5])

    def test_raises_tuple(self):
        with self.assertRaises(TypeError):
            task224((10, 5))

if __name__ == '__main__':
    unittest.main()
