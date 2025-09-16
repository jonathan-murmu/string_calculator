"""
String Calculator module.

This module implements a string calculator that follows the TDD Kata requirements.
"""
from string_calculator.interfaces import IInputParser, INumberValidator
from string_calculator.implementations import (
    DefaultInputParser,
    StandardDelimiterStrategy,
    CustomDelimiterStrategy,
    NegativeNumberValidator
)


class StringCalculator:
    """
    A class that provides string calculator functionality.
    
    This calculator can add numbers provided as a string with various delimiter options:
    - Default delimiters: comma and newline
    - Custom delimiter: specified with the format "//[delimiter]\n"
    
    This class follows the Dependency Inversion Principle by depending on abstractions
    rather than concrete implementations.
    """
    
    def __init__(
        self,
        parser: IInputParser = None,
        validator: INumberValidator = None
    ):
        """
        Initialize the StringCalculator with its dependencies.
        
        Args:
            parser (IInputParser, optional): The parser to use for input strings.
                Defaults to DefaultInputParser with standard strategies.
            validator (INumberValidator, optional): The validator to use for numbers.
                Defaults to NegativeNumberValidator.
        """
        # If no parser is provided, create a default one
        if parser is None:
            standard_strategy = StandardDelimiterStrategy()
            custom_strategy = CustomDelimiterStrategy()
            parser = DefaultInputParser(standard_strategy, custom_strategy)
        
        # If no validator is provided, create a default one
        if validator is None:
            validator = NegativeNumberValidator()
        
        self.parser = parser
        self.validator = validator
    
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
        
        # Parse the input to get the numbers
        numbers = self.parser.parse(numbers_str)
        
        # Validate numbers
        self.validator.validate(numbers)
        
        return sum(numbers)