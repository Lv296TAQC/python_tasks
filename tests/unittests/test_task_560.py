import unittest
from unittest.mock import patch
from tasks.task_560 import amicable


class TestsTask560(unittest.TestCase):

    @patch('tasks.task_330.minus_last', side_effect=range(100))
    def test_fifth_560(self, minus_last):
        self.assertEqual([(220, 284)], amicable())


if __name__ == '__main__':
    unittest.main()
