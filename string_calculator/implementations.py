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


class LongDelimiterStrategy(IDelimiterStrategy):
    """
    Long delimiter strategy that extracts a multi-character delimiter enclosed in square brackets.
    """
    
    def extract_delimiter_and_numbers(self, input_str: str) -> Tuple[str, str]:
        """
        Extract the long delimiter and numbers string from the input.
        
        Args:
            input_str (str): The input string to process, in the format "//[delimiter]\n[numbers]".
            
        Returns:
            Tuple[str, str]: A tuple containing (delimiter, numbers_str)
        """
        # Find the positions of the brackets and newline
        open_bracket = input_str.find('[')
        close_bracket = input_str.find(']')
        newline = input_str.find('\n')
        
        if open_bracket != -1 and close_bracket != -1 and newline != -1:
            # Extract the delimiter between the brackets
            delimiter = input_str[open_bracket + 1:close_bracket]
            # Extract the numbers string after the newline
            numbers_str = input_str[newline + 1:]

            numbers_str = numbers_str.replace('\n', delimiter)
            return delimiter, numbers_str
        
        return ',', input_str


class MultipleDelimiterStrategy(IDelimiterStrategy):
    """
    Multiple delimiter strategy that extracts multiple delimiters enclosed in square brackets.
    """
    
    def extract_delimiter_and_numbers(self, input_str: str) -> Tuple[str, str]:
        """
        Extract multiple delimiters and numbers string from the input.
        
        Args:
            input_str (str): The input string to process, in the format "//[delimiter1][delimiter2]...[delimiterN]\n[numbers]".
            
        Returns:
            Tuple[str, str]: A tuple containing (special_delimiter, numbers_str)
                             where all original delimiters are replaced with the special_delimiter
        """
        # Special marker to replace all delimiters
        special_delimiter = "__MULTI_DELIM__"
        
        # Find the position of the newline that separates delimiters from numbers
        newline_pos = input_str.find('\n')
        if newline_pos == -1:
            return ',', input_str
        
        # Extract the delimiters section and the numbers section
        delimiters_section = input_str[2:newline_pos]
        numbers_str = input_str[newline_pos + 1:]
        
        # Extract all delimiters enclosed in square brackets
        delimiters = []
        start_pos = 0
        while start_pos < len(delimiters_section):
            open_bracket = delimiters_section.find('[', start_pos)
            if open_bracket == -1:
                break
                
            close_bracket = delimiters_section.find(']', open_bracket)
            if close_bracket == -1:
                break
                
            delimiter = delimiters_section[open_bracket + 1:close_bracket]
            delimiters.append(delimiter)
            start_pos = close_bracket + 1
        
        # Replace all occurrences of each delimiter with the special delimiter
        for delimiter in delimiters:
            numbers_str = numbers_str.replace(delimiter, special_delimiter)
        
        # Replace newlines with the special delimiter as well
        numbers_str = numbers_str.replace('\n', special_delimiter)
        
        return special_delimiter, numbers_str


class DefaultInputParser(IInputParser):
    """
    Default implementation of the input parser.
    """
    
    def __init__(self, standard_strategy: IDelimiterStrategy, custom_strategy: IDelimiterStrategy,
                 long_delimiter_strategy: IDelimiterStrategy = None,
                 multiple_delimiter_strategy: IDelimiterStrategy = None):
        """
        Initialize the parser with delimiter strategies.
        
        Args:
            standard_strategy (IDelimiterStrategy): The strategy for standard delimiters.
            custom_strategy (IDelimiterStrategy): The strategy for custom delimiters.
            long_delimiter_strategy (IDelimiterStrategy, optional): The strategy for long delimiters.
            multiple_delimiter_strategy (IDelimiterStrategy, optional): The strategy for multiple delimiters.
        """
        self.standard_strategy = standard_strategy
        self.custom_strategy = custom_strategy
        self.long_delimiter_strategy = long_delimiter_strategy
        self.multiple_delimiter_strategy = multiple_delimiter_strategy
    
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
        
        # Determine which strategy to use based on the input format
        if input_str.startswith('//'):
            # Check if it's a multiple delimiter format (with multiple square brackets)
            if input_str.count('[') > 1 and input_str.count(']') > 1 and self.multiple_delimiter_strategy:
                delimiter, numbers_str = self.multiple_delimiter_strategy.extract_delimiter_and_numbers(input_str)
            # Check if it's a long delimiter format (with single square brackets)
            elif '[' in input_str and ']' in input_str and self.long_delimiter_strategy:
                delimiter, numbers_str = self.long_delimiter_strategy.extract_delimiter_and_numbers(input_str)
            else:
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
