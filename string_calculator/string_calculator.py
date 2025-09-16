"""
String Calculator module.

This module implements a string calculator that follows the TDD Kata requirements
using Object-Oriented Programming principles.
"""


class StringCalculator:
    """
    A class that provides string calculator functionality.
    
    This calculator can add numbers provided as a string with comma delimiters.
    """
    
    def add(self, numbers_str):
        """
        Add numbers provided as a string.
        
        Args:
            numbers_str (str): A string containing numbers separated by commas.
            
        Returns:
            int: The sum of the numbers.
        """
        if not numbers_str:
            return 0
        
        # Initial implementation - will be expanded through TDD
        return sum(int(num) for num in numbers_str.split(','))