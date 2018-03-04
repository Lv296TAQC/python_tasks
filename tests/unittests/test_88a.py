import unittest
from tasks.moo88a import task88a


class Test88(unittest.TestCase):
    def testAssertTrue(self):
        self.assertTrue(task88a(6))
        self.assertTrue(task88a(18))
        self.assertTrue(task88a(86))
    def testAssertFalse(self):
        self.assertFalse(task88a(5))
        self.assertFalse(task88a(17))
        self.assertFalse(task88a(87))


if __name__ == '__main__':
    unittest.main()
