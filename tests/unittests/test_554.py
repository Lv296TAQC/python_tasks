import unittest
from tasks.moo554 import task554


class Test554(unittest.TestCase):
    def test_task554(self):
        self.assertDictEqual({}, task554(0))
        self.assertDictEqual({1: [3, 4, 5]}, task554(10))
        self.assertDictEqual({1: [3, 4, 5], 2: [6, 8, 10]}, task554(11))
        self.assertDictEqual({1: [3, 4, 5], 2: [6, 8, 10]}, task554(13))
        self.assertDictEqual({1: [3, 4, 5], 2: [6, 8, 10], 3: [5, 12, 13]}, task554(14))
        with self.assertRaises(TypeError):
            task554(1.5)
            task554(qwer)

    def test_part_in_task554(self):
        self.assertIn([3, 4, 5], task554(100).values())
        self.assertIn([65, 72, 97], task554(100).values())
        self.assertIn([39, 80, 89], task554(100).values())
