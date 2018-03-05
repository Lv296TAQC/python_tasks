import unittest
from tasks.task_323 import task323


class Test323(unittest.TestCase):
    def test_list_for_2(self):
        self.assertListEqual([1], task323(2))

    def test_list_for_zero(self):
        self.assertListEqual([], task323(0))

    def test_list_for_minus_2(self):
        self.assertListEqual([], task323(-2))

    def test_list_for_6(self):
        self.assertListEqual([1, 5], task323(6))

    def test_list_for_8(self):
        self.assertListEqual([1, 3, 5, 7], task323(8))

    def test_list_for_41(self):
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, \
                              20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, \
                              37, 38, 39, 40], task323(41))

    def test_list_for_40(self):
        self.assertListEqual([1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39], \
                             task323(40))

    def test_raises_str(self):
        with self.assertRaises(TypeError):
            task323('qweqw')

    def test_raises_float(self):
        with self.assertRaises(TypeError):
            task323(10.5)

    def test_raises_list(self):
        with self.assertRaises(TypeError):
            task323([10, 5])

    def test_raises_tuple(self):
        with self.assertRaises(TypeError):
            task323((10, 5))


if __name__ == '__main__':
    unittest.main()
