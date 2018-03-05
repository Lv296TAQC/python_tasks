import unittest
from tasks.task_554 import task554


class Test554(unittest.TestCase):
    def test_task_dict_for_0(self):
        self.assertDictEqual({}, task554(0))

    def test_task_dict_for_10(self):
        self.assertDictEqual({1: [3, 4, 5]}, task554(10))

    def test_task_dict_for_minus_10(self):
        self.assertDictEqual({}, task554(-10))

    def test_task_dict_for_11(self):
        self.assertDictEqual({1: [3, 4, 5], 2: [6, 8, 10]}, task554(11))

    def test_task_dict_for_13(self):
        self.assertDictEqual({1: [3, 4, 5], 2: [6, 8, 10]}, task554(13))

    def test_task_dict_for_14(self):
        self.assertDictEqual({1: [3, 4, 5], 2: [6, 8, 10], 3: [5, 12, 13]}, task554(14))

    def test_raises_str(self):
        with self.assertRaises(TypeError):
            task554('qweqw')

    def test_raises_float(self):
        with self.assertRaises(TypeError):
            task554(10.5)

    def test_raises_list(self):
        with self.assertRaises(TypeError):
            task554([10, 5])

    def test_raises_tuple(self):
        with self.assertRaises(TypeError):
            task554((10, 5))

    def test_task554_part_in(self):
        self.assertIn([3, 4, 5], task554(100).values())
        self.assertIn([65, 72, 97], task554(100).values())
        self.assertIn([39, 80, 89], task554(100).values())


if __name__ == '__main__':
    unittest.main()
