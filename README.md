# String Calculator TDD Kata

A comprehensive implementation of the String Calculator TDD Kata in Python, following SOLID principles and Test-Driven Development practices.

## Project Overview

This project implements a String Calculator that can add numbers provided as a string with various delimiter options. The implementation follows the step-by-step approach of the TDD Kata, with each requirement implemented incrementally using Test-Driven Development.

The String Calculator is designed with a focus on:
- Clean, maintainable code
- SOLID principles
- Interface-based design
- Separation of concerns
- Extensibility

## Requirements Implemented

The String Calculator implements all the requirements of the TDD Kata:

1. **Basic Addition**: The method can take 0, 1, or 2 numbers separated by commas and return their sum
   - Example: "" returns 0, "1" returns 1, "1,2" returns 3

2. **Multiple Numbers**: The add method can handle an unknown number of arguments
   - Example: "1,2,3,4,5" returns 15

3. **Newline Delimiters**: The add method can handle new lines between numbers (instead of commas)
   - Example: "1\n2,3" returns 6

4. **Custom Delimiters**: Support for different delimiters specified at the beginning of the string
   - Example: "//;\n1;2" returns 3

5. **Negative Number Validation**: Calling add with negative numbers will throw an exception with the message "negative numbers not allowed" and the negative numbers
   - Example: "-1,2" throws "negative numbers not allowed: -1"

6. **Upper Limit Filtering**: Numbers greater than 1000 are ignored
   - Example: "2,1001" returns 2

7. **Long Delimiters**: Delimiters can be of any length when enclosed in square brackets
   - Example: "//[***]\n1***2***3" returns 6

8. **Multiple Delimiters**: Allow multiple delimiters enclosed in square brackets
   - Example: "//[*][%]\n1*2%3" returns 6

## Architecture Overview

The project follows a clean architecture with interfaces and implementations separated to promote loose coupling and high cohesion.

### Core Components

#### Interfaces

- **IInputParser**: Responsible for parsing input strings into a list of integers
- **IDelimiterStrategy**: Responsible for extracting delimiters and number strings from the input
- **INumberValidator**: Responsible for validating the list of numbers according to rules

### Class Relationships

```
StringCalculator
├── IInputParser (DefaultInputParser)
│   ├── IDelimiterStrategy (StandardDelimiterStrategy)
│   ├── IDelimiterStrategy (CustomDelimiterStrategy)
│   ├── IDelimiterStrategy (LongDelimiterStrategy)
│   └── IDelimiterStrategy (MultipleDelimiterStrategy)
└── INumberValidator (CompositeValidator)
    ├── INumberValidator (NegativeNumberValidator)
    └── INumberValidator (UpperLimitNumberValidator)
```

## Setup and Usage

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:

2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running Tests

Run the tests using pytest:

```
pytest
```

For test coverage report:

```
pytest --cov=string_calculator
```

### Usage Examples

```python
from string_calculator.string_calculator import StringCalculator

# Create a calculator instance
calculator = StringCalculator()

# Basic usage
result = calculator.add("1,2,3")  # Returns 6

# Using newlines as delimiters
result = calculator.add("1\n2,3")  # Returns 6

# Using custom delimiter
result = calculator.add("//;\n1;2")  # Returns 3

# Using long delimiter
result = calculator.add("//[***]\n1***2***3")  # Returns 6

# Using multiple delimiters
result = calculator.add("//[*][%]\n1*2%3")  # Returns 6

# Numbers greater than 1000 are ignored
result = calculator.add("2,1001")  # Returns 2

# Negative numbers throw an exception
try:
    calculator.add("-1,2")
except ValueError as e:
    print(e)  # Prints "negative numbers not allowed: -1"
```
