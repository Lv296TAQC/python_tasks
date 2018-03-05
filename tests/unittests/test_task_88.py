import unittest
from tasks.task_88 import three_go_in


class TestsTask88a(unittest.TestCase):

    def test_first_88(self):
        self.assertTrue(three_go_in(19))
        self.assertFalse(three_go_in(2))
        self.assertRaises(TypeError, three_go_in, 'abc')
        self.assertRaises(TypeError, three_go_in, (4, 3))
        self.assertRaises(TypeError, three_go_in, {1: 3})
        self.assertRaises(TypeError, three_go_in, {8, 2})
        self.assertRaises(TypeError, three_go_in, [1, 3])
        self.assertRaises(TypeError, three_go_in)
        self.assertRaises(TypeError, three_go_in, False)  # Should give us TypeError(Ask)


if __name__ == '__main__':
    unittest.main()
