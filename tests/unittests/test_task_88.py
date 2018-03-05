import unittest
from tasks.task_88 import three_go_in


class TestsTask88a(unittest.TestCase):

    def test_first_88(self):
        self.assertTrue(three_go_in(19))
        self.assertFalse(three_go_in(2))


if __name__ == '__main__':
    unittest.main()
