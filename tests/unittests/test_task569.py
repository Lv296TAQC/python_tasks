from tasks import task_569
import unittest


class TestTask(unittest.TestCase):
    def test_is_prime(self):
        self.assertEquals(task_569.is_prime(123))

if __name__ == '__main__':
    unittest.main()
