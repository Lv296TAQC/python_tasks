import unittest
from tasks.task_178_b import multiple_numbers


class TestTask178b(unittest.TestCase):

    def test_normal_args(self):
        self.assertEqual(multiple_numbers([6, 21, 96, 110]), 3)
        self.assertEqual(multiple_numbers([-110, 5, 78]), 0)
        self.assertEqual(multiple_numbers([1, 8, 6, 1, 5, 78]), 1)

    def test_str_arg(self):
        self.assertRaises(TypeError, multiple_numbers(''))
        self.assertRaises(TypeError, multiple_numbers('58, -64, 9, 11'))


if __name__ == '__main__':
    unittest.main()
