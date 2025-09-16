"""
Implementations of the interfaces for the String Calculator.

This module provides concrete implementations of the interfaces.
"""
from typing import List, Tuple

from string_calculator.interfaces import IInputParser, IDelimiterStrategy, INumberValidator


class StandardDelimiterStrategy(IDelimiterStrategy):
    """
    Standard delimiter strategy that uses comma and newline as delimiters.
    """
    
    def extract_delimiter_and_numbers(self, input_str: str) -> Tuple[str, str]:
        """
        Extract the standard delimiter (comma) and numbers string.
        
        Args:
            input_str (str): The input string to process.
            
        Returns:
            Tuple[str, str]: A tuple containing (delimiter, numbers_str)
        """
        # Replace newlines with commas
        numbers_str = input_str.replace('\n', ',')
        return ',', numbers_str


class CustomDelimiterStrategy(IDelimiterStrategy):
    """
    Custom delimiter strategy that extracts a user-defined delimiter from the input.
    """
    
    def extract_delimiter_and_numbers(self, input_str: str) -> Tuple[str, str]:
        """
        Extract the custom delimiter and numbers string from the input.
        
        Args:
            input_str (str): The input string to process, in the format "//[delimiter]\n[numbers]".
            
        Returns:
            Tuple[str, str]: A tuple containing (delimiter, numbers_str)
        """
        delimiter_end = input_str.find('\n')
        if delimiter_end != -1:
            delimiter = input_str[2:delimiter_end]
            numbers_str = input_str[delimiter_end + 1:]
            # Replace newlines with the delimiter
            numbers_str = numbers_str.replace('\n', delimiter)
            return delimiter, numbers_str
        
        # This should not happen with valid input
        return ',', input_str


class DefaultInputParser(IInputParser):
    """
    Default implementation of the input parser.
    """
    
    def __init__(self, standard_strategy: IDelimiterStrategy, custom_strategy: IDelimiterStrategy):
        """
        Initialize the parser with delimiter strategies.
        
        Args:
            standard_strategy (IDelimiterStrategy): The strategy for standard delimiters.
            custom_strategy (IDelimiterStrategy): The strategy for custom delimiters.
        """
        self.standard_strategy = standard_strategy
        self.custom_strategy = custom_strategy
    
    def parse(self, input_str: str) -> List[int]:
        """
        Parse the input string into a list of integers.
        
        Args:
            input_str (str): The input string to parse.
            
        Returns:
            List[int]: The list of parsed integers.
        """
        if not input_str:
            return []
        
        # Determine which strategy to use based on whether the input has a custom delimiter
        if input_str.startswith('//'):
            delimiter, numbers_str = self.custom_strategy.extract_delimiter_and_numbers(input_str)
        else:
            delimiter, numbers_str = self.standard_strategy.extract_delimiter_and_numbers(input_str)
        
        # Split by the delimiter and convert to integers
        return [int(num) for num in numbers_str.split(delimiter) if num]


class NegativeNumberValidator(INumberValidator):
    """
    Validator that checks for negative numbers.
    """
    
    def validate(self, numbers: List[int]) -> None:
        """
        Validate that there are no negative numbers in the list.
        
        Args:
            numbers (List[int]): The list of numbers to validate.
            
        Raises:
            ValueError: If any negative numbers are found.
        """
        negative_numbers = [num for num in numbers if num < 0]
        if negative_numbers:
            negative_numbers_str = ", ".join(str(num) for num in negative_numbers)
            raise ValueError(f"negative numbers not allowed: {negative_numbers_str}")
        

class UpperLimitNumberValidator(INumberValidator):
    """
    Validator that filters out numbers greater than 1000.
    """
    
    def __init__(self, upper_limit=1000):
        """
        Initialize the validator with an upper limit.
        
        Args:
            upper_limit (int, optional): The upper limit for numbers. Defaults to 1000.
        """
        self.upper_limit = upper_limit
    
    def validate(self, numbers: List[int]) -> None:
        """
        This validator doesn't raise exceptions but is meant to be used
        to filter numbers in the calculator.
        
        Args:
            numbers (List[int]): The list of numbers to validate.
        """
        # This validator doesn't raise exceptions
        pass


class CompositeValidator(INumberValidator):
    """
    A validator that combines multiple validators.
    """
    
    def __init__(self, validators: List[INumberValidator]):
        """
        Initialize with a list of validators.
        
        Args:
            validators (List[INumberValidator]): The validators to use.
        """
        self.validators = validators
    
    def validate(self, numbers: List[int]) -> None:
        """
        Run all validators on the numbers.
        
        Args:
            numbers (List[int]): The list of numbers to validate.
            
        Raises:
            ValueError: If any validator raises an exception.
        """
        for validator in self.validators:
            validator.validate(numbers)
