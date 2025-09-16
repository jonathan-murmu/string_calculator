"""
Tests for the number validator.
"""
import unittest
from string_calculator.implementations import NegativeNumberValidator


class TestNegativeNumberValidator(unittest.TestCase):
    """Test cases for the NegativeNumberValidator class."""

    def setUp(self):
        """Set up a new NegativeNumberValidator instance for each test."""
        self.validator = NegativeNumberValidator()

    def test_validate_positive_numbers(self):
        """Test validation with only positive numbers."""
        # Should not raise any exception
        self.validator.validate([1, 2, 3])

    def test_validate_zero(self):
        """Test validation with zero."""
        # Should not raise any exception
        self.validator.validate([0, 1, 2])

    def test_validate_single_negative_number(self):
        """Test validation with a single negative number."""
        with self.assertRaises(ValueError) as context:
            self.validator.validate([-1, 2, 3])
        
        self.assertEqual("negative numbers not allowed: -1", str(context.exception))

    def test_validate_multiple_negative_numbers(self):
        """Test validation with multiple negative numbers."""
        with self.assertRaises(ValueError) as context:
            self.validator.validate([-1, -2, 3])
        
        self.assertEqual("negative numbers not allowed: -1, -2", str(context.exception))

    def test_validate_all_negative_numbers(self):
        """Test validation with all negative numbers."""
        with self.assertRaises(ValueError) as context:
            self.validator.validate([-1, -2, -3])
        
        self.assertEqual("negative numbers not allowed: -1, -2, -3", str(context.exception))


if __name__ == "__main__":
    unittest.main()