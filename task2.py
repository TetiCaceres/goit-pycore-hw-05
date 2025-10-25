from typing import Callable
import re


def generator_numbers(text: str):
    """
    Generator function that yields all real numbers found in the input text.
    Real numbers are integers or decimals, possibly negative, and separated by spaces.
    """
    # Regular expression pattern for real numbers (integer or decimal)
    pattern = r'-?\d+(?:\.\d+)?'

    # Split the text into words and iterate through each word
    for word in text.split():
        # Check if the word fully matches the real number pattern
        if re.fullmatch(pattern, word):
            # Convert the word to float and yield it
            yield float(word)


def sum_profit(text: str, func: Callable):
    """
    Calculate the total sum of all real numbers in the input text.
    
    Args:
        text (str): Input string containing numbers.
        func (Callable): Generator function that yields numbers from the text.

    Returns:
        float: Sum of all numbers found.
    """
    # Use the generator directly in sum() for efficient calculation
    total = sum(func(text))
    return total


# Example usage
text = (
    "Загальний дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
)
total_income = sum_profit(text, generator_numbers)

# Print the total income
print(f"Загальний дохід: {total_income}")
