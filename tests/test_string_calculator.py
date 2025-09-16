"""
Test module for the StringCalculator class.
"""

import unittest
from string_calculator.string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    """Test cases for the StringCalculator class."""

    def setUp(self):
        """Set up a new StringCalculator instance for each test."""
        self.calculator = StringCalculator()

    def test_empty_string_returns_zero(self):
        """Test that an empty string returns 0."""
        self.assertEqual(0, self.calculator.add(""))

    def test_single_number_returns_value(self):
        """Test that a single number returns its value."""
        self.assertEqual(1, self.calculator.add("1"))
        self.assertEqual(5, self.calculator.add("5"))

    def test_two_numbers_returns_sum(self):
        """Test that two numbers separated by a comma return their sum."""
        self.assertEqual(3, self.calculator.add("1,2"))
        self.assertEqual(10, self.calculator.add("7,3"))


    def test_multiple_numbers_returns_sum(self):
        """Test that multiple numbers separated by commas return their sum."""
        self.assertEqual(6, self.calculator.add("1,2,3"))
        self.assertEqual(15, self.calculator.add("1,2,3,4,5"))
        self.assertEqual(55, self.calculator.add("1,2,3,4,5,6,7,8,9,10"))


    def test_newline_as_delimiter(self):
        """Test that newlines can be used as delimiters, just like commas."""
        self.assertEqual(6, self.calculator.add("1\n2,3"))
        self.assertEqual(10, self.calculator.add("4\n6"))
        self.assertEqual(15, self.calculator.add("1\n2\n3,4,5"))


if __name__ == "__main__":
    unittest.main()