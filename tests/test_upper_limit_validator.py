"""
Tests for the upper limit number validator.
"""
import unittest
from string_calculator.implementations import UpperLimitNumberValidator


class TestUpperLimitNumberValidator(unittest.TestCase):
    """Test cases for the UpperLimitNumberValidator class."""

    def setUp(self):
        """Set up a new UpperLimitNumberValidator instance for each test."""
        self.validator = UpperLimitNumberValidator()

    def test_validate_numbers_below_limit(self):
        """Test validation with numbers below the limit."""
        # Should not raise any exception
        self.validator.validate([1, 2, 3, 1000])

    def test_validate_numbers_above_limit(self):
        """Test validation with numbers above the limit."""
        # Should not raise any exception (this validator doesn't raise exceptions)
        self.validator.validate([1, 2, 1001, 2000])

    def test_custom_upper_limit(self):
        """Test validation with a custom upper limit."""
        custom_validator = UpperLimitNumberValidator(upper_limit=500)
        # Should not raise any exception
        custom_validator.validate([1, 501, 1000])


if __name__ == "__main__":
    unittest.main()