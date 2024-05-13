# This is a simple script that demonstrates PEP8 compliance

# Import standard library modules
import os
import sys

# Import third-party modules
import requests

# Import local modules
from utils import helper_function


# Constants should be uppercase
API_URL = "https://api.example.com"


def main():
    """Main function of the script."""
    # Variable names should be lowercase with words separated by underscores
    user_name = "John"

    # Use 4 spaces for indentation
    for i in range(5):
        # Use descriptive variable names
        print(f"Hello, {user_name}! This is iteration {i}")

    # Use explicit comparisons
    if os.path.exists("file.txt"):
        # Use context managers for file operations
        with open("file.txt", "r") as file:
            contents = file.read()
        print(contents)

    # Use list comprehensions when appropriate
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = [num ** 2 for num in numbers]
    print(squared_numbers)

    # Use docstrings to document functions and classes
    def example_function(argument):
        """This is an example function."""
        return argument * 2

    # Function calls should be separated by blank lines
    result = example_function(10)
    print(result)

    # Use single quotes for string literals
    api_response = requests.get(API_URL)
    print(api_response.json())

    # Call a helper function from a separate module
    helper_function()


# Ensure that the main function is called if this script is executed directly
if __name__ == "__main__":
    main()

