"""
Tests for the composite validator.
"""
import unittest
from string_calculator.implementations import (
    CompositeValidator,
    NegativeNumberValidator,
    UpperLimitNumberValidator
)


class TestCompositeValidator(unittest.TestCase):
    """Test cases for the CompositeValidator class."""

    def setUp(self):
        """Set up a new CompositeValidator instance for each test."""
        negative_validator = NegativeNumberValidator()
        upper_limit_validator = UpperLimitNumberValidator()
        self.validator = CompositeValidator([negative_validator, upper_limit_validator])

    def test_validate_valid_numbers(self):
        """Test validation with valid numbers."""
        # Should not raise any exception
        self.validator.validate([1, 2, 3, 1000])

    def test_validate_negative_numbers(self):
        """Test validation with negative numbers."""
        with self.assertRaises(ValueError) as context:
            self.validator.validate([-1, 2, 3])
        
        self.assertEqual("negative numbers not allowed: -1", str(context.exception))

    def test_validate_numbers_above_limit(self):
        """Test validation with numbers above the limit."""
        # Should not raise an exception, but the upper limit validator will be used
        # in the calculator to filter these numbers
        self.validator.validate([1, 2, 1001])


if __name__ == "__main__":
    unittest.main()