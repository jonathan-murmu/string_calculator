# String Calculator

A TDD Kata implementation of a String Calculator in Python.

## Project Description

This project implements a String Calculator following Test-Driven Development (TDD) principles. The String Calculator can add numbers provided as a string with comma delimiters.


## Setup

1. Create a virtual environment (recommended)

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running Tests

Run the tests using pytest:

```
pytest
```

For test coverage report:

```
pytest --cov=string_calculator
```

## String Calculator Requirements

The String Calculator should follow these rules:

1. The method can take 0, 1, or 2 numbers separated by commas and return their sum
   - Example: "" returns 0, "1" returns 1, "1,2" returns 3
2. Allow the add method to handle an unknown number of arguments
3. Allow the add method to handle new lines between numbers (instead of commas)
4. Support different delimiters
5. Calling add with negative numbers will throw an exception
6. Numbers greater than 1000 should be ignored
7. Delimiters can be of any length
8. Allow multiple delimiters

