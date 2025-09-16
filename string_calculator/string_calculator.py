"""
String Calculator module.

This module implements a string calculator that follows the TDD Kata requirements
using Object-Oriented Programming principles.
"""


class StringCalculator:
    """
    A class that provides string calculator functionality.
    
    This calculator can add numbers provided as a string with comma or newline delimiters.
    """
    
    def add(self, numbers_str):
        """
        Add numbers provided as a string.
        
        Args:
            numbers_str (str): A string containing numbers separated by commas or newlines.
            
        Returns:
            int: The sum of the numbers.
        """
        if not numbers_str:
            return 0
        
        # Replace newlines with commas, then split by commas
        numbers_str = numbers_str.replace('\n', ',')
        
        # Implementation handles any number of comma-separated values
        return sum(int(num) for num in numbers_str.split(','))