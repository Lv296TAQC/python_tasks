""""Test for task5_562"""


from unittest import TestCase
from unittest.mock import patch

from tasks.task_562 import split_into_digits, get_armstrong_numbs


class TestsTask562(TestCase):
    """
        Test to check if function split_into_digits is splitting given natural
        number into digits, and if function get_armstrong_numbs founds the right
        and complete list of armstrong's numbers, which consists of 2, 3 and four digits.
    """

    def test_split_into_digits_first_a(self):
        """Check if expected results correspond to actual with a specific input"""
        int_ = 120
        res = split_into_digits(int_)
        self.assertEqual(res, [1, 2, 0])

    def test_split_into_digits_first_b(self):
        """Check if expected results correspond to actual with a specific input"""
        int_ = 1
        res = split_into_digits(int_)
        self.assertEqual(res, [1])

    def test_split_into_digits_first_c(self):
        """Check if expected results correspond to actual with a specific input"""
        int_ = 9876543210
        res = split_into_digits(int_)
        self.assertEqual(res, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

    def test_split_into_digits_second_a(self):
        """Test to check if input and output types of values correspond to
        intended, according to the function docstrings.
        """
        int_ = 100
        split_into_digits(int_)
        self.assertIsInstance(int_, int)

    def test_split_into_digits_second_b(self):
        """Test to check if input and output types of values correspond to
        intended, according to the function docstrings.
        """
        int_ = 100
        res = split_into_digits(int_)
        self.assertIsInstance(res, list)

    def test_split_into_digits_third_a(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(TypeError, split_into_digits, "kal-el")

    def test_split_into_digits_third_b(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(ValueError, split_into_digits, -1000)

    def test_get_armstrong_first_a(self):
        """Check if expected results correspond to actual with a specific input"""
        left = 22
        right = 4444
        res = get_armstrong_numbs(left, right)
        self.assertEqual(res, [153, 370, 371, 407, 1634])

    def test_get_armstrong_first_b(self):
        """Check if expected results correspond to actual with a specific input"""
        left = 10
        right = 9999
        res = get_armstrong_numbs(left, right)
        self.assertEqual(res, [153, 370, 371, 407, 1634, 8208, 9474])
        self.assertEqual(len(res), 7)

    def test_get_armstrong_second_a(self):
        """Test to check if input and output types of values correspond to
        intended, according to the function docstrings.
        """
        left = 99
        right = 1000
        res = get_armstrong_numbs(left, right)
        self.assertIsInstance(left, int)
        self.assertIsInstance(right, int)
        self.assertIsInstance(res, list)

    def test_get_armstrong_second_b(self):
        """Test to check if input and output types of values correspond to
        intended, according to the function docstrings.
        """
        left = 99
        right = 1000
        res = get_armstrong_numbs(left, right)
        self.assertIsInstance(res, list)

    def test_get_armstrong_third_a(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(TypeError, get_armstrong_numbs, "joer-el", "cryot")

    def test_get_armstrong_third_b(self):
        """Test to check if expected Error raises when input is not valid"""
        self.assertRaises(ValueError, get_armstrong_numbs, -1000, 1000)

    @patch('tasks.task_562.split_into_digits', return_value=[4, 0, 7])
    def test_get_armstrong_fourth(self, split_into_digits):    # pylint: disable=W0621
        """Check if expected results correspond to actual with a specific input, which isn't
        intended to change result hence mocked function split_into_digits"""
        left = 10
        right = 9999
        res = get_armstrong_numbs(left, right)
        self.assertEqual(split_into_digits(407), [4, 0, 7])
        self.assertEqual(res, [407])
