import unittest
from tasks.task_178b import count_sq


class TestsTask178b(unittest.TestCase):

    def test_second_b_178(self):
        self.assertEqual(3, count_sq((1, 2, 3, 5, 6, 36, 4, 16)))
        self.assertRaises(TypeError, count_sq, 'abc')
        self.assertRaises(TypeError, count_sq, {'346'})
        self.assertRaises(TypeError, count_sq, 8)
        self.assertRaises(TypeError, count_sq)
        self.assertRaises(TypeError, count_sq, False)


if __name__ == '__main__':
    unittest.main()
