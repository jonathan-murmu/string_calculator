"""
Tests for the delimiter strategies.
"""
import unittest
from string_calculator.implementations import StandardDelimiterStrategy, CustomDelimiterStrategy


class TestStandardDelimiterStrategy(unittest.TestCase):
    """Test cases for the StandardDelimiterStrategy class."""

    def setUp(self):
        """Set up a new StandardDelimiterStrategy instance for each test."""
        self.strategy = StandardDelimiterStrategy()

    def test_extract_delimiter_and_numbers_simple(self):
        """Test extraction with simple comma-separated numbers."""
        delimiter, numbers_str = self.strategy.extract_delimiter_and_numbers("1,2,3")
        self.assertEqual(',', delimiter)
        self.assertEqual('1,2,3', numbers_str)

    def test_extract_delimiter_and_numbers_with_newlines(self):
        """Test extraction with newlines in the input."""
        delimiter, numbers_str = self.strategy.extract_delimiter_and_numbers("1\n2,3")
        self.assertEqual(',', delimiter)
        self.assertEqual('1,2,3', numbers_str)

    def test_extract_delimiter_and_numbers_only_newlines(self):
        """Test extraction with only newlines as separators."""
        delimiter, numbers_str = self.strategy.extract_delimiter_and_numbers("1\n2\n3")
        self.assertEqual(',', delimiter)
        self.assertEqual('1,2,3', numbers_str)


class TestCustomDelimiterStrategy(unittest.TestCase):
    """Test cases for the CustomDelimiterStrategy class."""

    def setUp(self):
        """Set up a new CustomDelimiterStrategy instance for each test."""
        self.strategy = CustomDelimiterStrategy()

    def test_extract_delimiter_and_numbers_semicolon(self):
        """Test extraction with semicolon as custom delimiter."""
        delimiter, numbers_str = self.strategy.extract_delimiter_and_numbers("//;\n1;2;3")
        self.assertEqual(';', delimiter)
        self.assertEqual('1;2;3', numbers_str)

    def test_extract_delimiter_and_numbers_pipe(self):
        """Test extraction with pipe as custom delimiter."""
        delimiter, numbers_str = self.strategy.extract_delimiter_and_numbers("//|\n1|2|3")
        self.assertEqual('|', delimiter)
        self.assertEqual('1|2|3', numbers_str)

    def test_extract_delimiter_and_numbers_with_newlines(self):
        """Test extraction with newlines in the numbers part."""
        delimiter, numbers_str = self.strategy.extract_delimiter_and_numbers("//;\n1;2\n3")
        self.assertEqual(';', delimiter)
        self.assertEqual('1;2;3', numbers_str)


class TestLongDelimiterStrategy(unittest.TestCase):
    """Test cases for the LongDelimiterStrategy class."""

    def setUp(self):
        """Set up a new LongDelimiterStrategy instance for each test."""
        from string_calculator.implementations import LongDelimiterStrategy
        self.strategy = LongDelimiterStrategy()

    def test_extract_delimiter_and_numbers_long_delimiter(self):
        """Test extraction with a long delimiter enclosed in square brackets."""
        delimiter, numbers_str = self.strategy.extract_delimiter_and_numbers("//[***]\n1***2***3")
        self.assertEqual('***', delimiter)
        self.assertEqual('1***2***3', numbers_str)

    def test_extract_delimiter_and_numbers_multiple_characters(self):
        """Test extraction with a delimiter containing multiple different characters."""
        delimiter, numbers_str = self.strategy.extract_delimiter_and_numbers("//[==;]\n1==;2==;3")
        self.assertEqual('==;', delimiter)
        self.assertEqual('1==;2==;3', numbers_str)

    def test_extract_delimiter_and_numbers_with_newlines(self):
        """Test extraction with newlines in the numbers part."""
        delimiter, numbers_str = self.strategy.extract_delimiter_and_numbers("//[***]\n1***2\n3")
        self.assertEqual('***', delimiter)
        self.assertEqual('1***2***3', numbers_str)


if __name__ == "__main__":
    unittest.main()