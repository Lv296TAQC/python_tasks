from tasks.task_184 import update
import unittest


class TestTask184(unittest.TestCase):
    def test_update_function(self):
        self.assertEquals(update(43, 12, [12, 34, 43]), [0, 34, 43])

    def test_update_value(self):
        self.assertEquals(update(21233, 23, [21, 23, 43]), [21, 0, 43])

    def test_update_failure(self):
        self.assertEquals(update(-1, 23, [21, 23, 43]), 'incorrect values')

    def test_update_raise(self):
        with self.assertRaises(TypeError):
            update(23.5, 12[12, 123, 4234])

    def test_update_str(self):
        with self.assertRaises(TypeError):
            update('ste', 123[12, 123, 4234])

