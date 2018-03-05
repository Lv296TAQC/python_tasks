import unittest
from tasks.task_107 import task107


class Test107(unittest.TestCase):
    def test_equal_3(self):
        self.assertEqual(0, task107(3))

    def test_equal_15(self):
        self.assertEqual(1, task107(15))

    def test_equal_63(self):
        self.assertEqual(2, task107(63))

    def test_equal_64(self):
        self.assertEqual(2, task107(64))

    def test_equal_65(self):
        self.assertEqual(3, task107(65))

    def test_int_minus(self):
        minus = -6
        self.assertLess(4 ** task107(minus), minus)

    def test_raises_str(self):
        with self.assertRaises(TypeError):
            task107('qweqw')

    def test_raises_float(self):
        with self.assertRaises(TypeError):
            task107(10.5)

    def test_raises_list(self):
        with self.assertRaises(TypeError):
            task107([10, 5])

    def test_raises_tuple(self):
        with self.assertRaises(TypeError):
            task107((10, 5))

    def test_type_return(self):
        self.assertIsInstance(task107(9), int)


if __name__ == '__main__':
    unittest.main()
