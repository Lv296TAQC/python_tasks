import unittest
from tasks.task_242 import total_sum


class TestTask242(unittest.TestCase):
    def test_true(self):
        self.assertTrue(total_sum(4))


if __name__ == '__main__':
    unittest.main()
