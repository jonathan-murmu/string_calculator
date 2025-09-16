"""
Interfaces for the String Calculator.
"""
from abc import ABC, abstractmethod
from typing import List, Tuple


class IInputParser(ABC):
    """Interface for parsing input strings in the calculator."""
    
    @abstractmethod
    def parse(self, input_str: str) -> List[int]:
        """
        Parse the input string into a list of integers.
        
        Args:
            input_str (str): The input string to parse.
            
        Returns:
            List[int]: The list of parsed integers.
        """
        pass


class IDelimiterStrategy(ABC):
    """Interface for delimiter strategies in the calculator."""
    
    @abstractmethod
    def extract_delimiter_and_numbers(self, input_str: str) -> Tuple[str, str]:
        """
        Extract the delimiter and numbers string from the input.
        
        Args:
            input_str (str): The input string to process.
            
        Returns:
            Tuple[str, str]: A tuple containing (delimiter, numbers_str)
        """
        pass


class INumberValidator(ABC):
    """Interface for number validation in the calculator."""
    
    @abstractmethod
    def validate(self, numbers: List[int]) -> None:
        """
        Validate the list of numbers according to the rules.
        
        Args:
            numbers (List[int]): The list of numbers to validate.
            
        Raises:
            ValueError: If any validation rule is violated.
        """
        pass