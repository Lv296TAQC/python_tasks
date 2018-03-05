import mock
import unittest
from tasks.task_560 import amicable


class TestsTask560(unittest.TestCase):

    def test_fifth_560(self):
        """Ask how to implement side_effect for minus_last in loop"""
        with mock.patch('tasks.fourth_330.minus_last', side_effect=[5, 6, 7]):
            self.assertEqual([(220, 284)], amicable())


if __name__ == '__main__':
    unittest.main()
