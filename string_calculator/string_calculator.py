"""
String Calculator module.

This module implements a string calculator that follows the TDD Kata requirements
using Object-Oriented Programming principles.
"""


class StringCalculator:
    """
    A class that provides string calculator functionality.
    
    This calculator can add numbers provided as a string with various delimiter options:
    - Default delimiters: comma and newline
    - Custom delimiter: specified with the format "//[delimiter]\n"
    """
    
    def _parse_input(self, numbers_str):
        """
        Parse the input string to extract the delimiter and the numbers.
        
        Args:
            numbers_str (str): The input string to parse.
            
        Returns:
            tuple: A tuple containing (delimiter, parsed_numbers_str)
        """
        # Default delimiter
        delimiter = ','
        
        # Check for custom delimiter
        if numbers_str.startswith('//'):
            delimiter_end = numbers_str.find('\n')
            if delimiter_end != -1:
                delimiter = numbers_str[2:delimiter_end]
                numbers_str = numbers_str[delimiter_end + 1:]
        
        # Replace newlines with the delimiter
        numbers_str = numbers_str.replace('\n', delimiter)
        
        return delimiter, numbers_str
    
    def add(self, numbers_str):
        """
        Add numbers provided as a string.
        
        Args:
            numbers_str (str): A string containing numbers separated by delimiters.
                               Supports commas and newlines as default delimiters.
                               Can specify a custom delimiter with the format "//[delimiter]\n".
            
        Returns:
            int: The sum of the numbers.
        """
        if not numbers_str:
            return 0
        
        # Parse the input to get the delimiter and the numbers string
        delimiter, parsed_numbers_str = self._parse_input(numbers_str)
        
        # Split by the delimiter and sum the numbers
        return sum(int(num) for num in parsed_numbers_str.split(delimiter))