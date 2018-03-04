import unittest
from tasks.moo107 import task107


class Test107(unittest.TestCase):
    def testEqual(self):
        self.failUnlessEqual(0, task107(3))

        self.failUnlessEqual(1, task107(15))
        self.failUnlessEqual(2, task107(63))
        self.failUnlessEqual(2, task107(64))
        self.failUnlessEqual(3, task107(65))

if __name__ == '__main__':
    unittest.main()
