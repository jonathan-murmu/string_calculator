"""
Tests for the input parser.
"""
import unittest
from string_calculator.implementations import (
    DefaultInputParser,
    StandardDelimiterStrategy,
    CustomDelimiterStrategy,
    LongDelimiterStrategy
)


class TestDefaultInputParser(unittest.TestCase):
    """Test cases for the DefaultInputParser class."""

    def setUp(self):
        """Set up a new DefaultInputParser instance for each test."""
        standard_strategy = StandardDelimiterStrategy()
        custom_strategy = CustomDelimiterStrategy()
        long_delimiter_strategy = LongDelimiterStrategy()
        self.parser = DefaultInputParser(standard_strategy, custom_strategy, long_delimiter_strategy)

    def test_parse_empty_string(self):
        """Test parsing an empty string."""
        result = self.parser.parse("")
        self.assertEqual([], result)

    def test_parse_single_number(self):
        """Test parsing a single number."""
        result = self.parser.parse("1")
        self.assertEqual([1], result)

    def test_parse_multiple_numbers_comma_separated(self):
        """Test parsing multiple comma-separated numbers."""
        result = self.parser.parse("1,2,3")
        self.assertEqual([1, 2, 3], result)

    def test_parse_multiple_numbers_newline_separated(self):
        """Test parsing multiple newline-separated numbers."""
        result = self.parser.parse("1\n2\n3")
        self.assertEqual([1, 2, 3], result)

    def test_parse_mixed_separators(self):
        """Test parsing with mixed separators (commas and newlines)."""
        result = self.parser.parse("1\n2,3")
        self.assertEqual([1, 2, 3], result)

    def test_parse_custom_delimiter(self):
        """Test parsing with a custom delimiter."""
        result = self.parser.parse("//;\n1;2;3")
        self.assertEqual([1, 2, 3], result)

    def test_parse_custom_delimiter_with_newlines(self):
        """Test parsing with a custom delimiter and newlines in the numbers."""
        result = self.parser.parse("//;\n1;2\n3")
        self.assertEqual([1, 2, 3], result)

    def test_parse_negative_numbers(self):
        """Test parsing negative numbers (validation is handled separately)."""
        result = self.parser.parse("-1,2,-3")
        self.assertEqual([-1, 2, -3], result)

    def test_parse_long_delimiter(self):
        """Test parsing with a long delimiter enclosed in square brackets."""
        result = self.parser.parse("//[***]\n1***2***3")
        self.assertEqual([1, 2, 3], result)

    def test_parse_long_delimiter_with_special_chars(self):
        """Test parsing with a long delimiter containing special characters."""
        result = self.parser.parse("//[==;]\n1==;2==;3")
        self.assertEqual([1, 2, 3], result)

    def test_parse_long_delimiter_with_newlines(self):
        """Test parsing with a long delimiter and newlines in the numbers."""
        result = self.parser.parse("//[***]\n1***2\n3")
        self.assertEqual([1, 2, 3], result)


if __name__ == "__main__":
    unittest.main()