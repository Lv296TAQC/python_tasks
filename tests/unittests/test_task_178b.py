import unittest
from tasks.task_178b import count_sq


class Test178b(unittest.TestCase):

    def test_second_b_178(self):
        self.assertEqual(3, count_sq((1, 2, 3, 5, 6, 36, 4, 16)))


if __name__ == '__main__':
    unittest.main()
