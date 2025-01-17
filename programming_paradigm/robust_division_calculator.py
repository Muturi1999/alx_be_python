#!/usr/bin/env python3

def safe_divide(numerator, denominator):
    """
    Perform division with error handling.

    Args:
        numerator (str): The numerator, as a string (to convert to float).
        denominator (str): The denominator, as a string (to convert to float).

    Returns:
        str: The result of the division or an appropriate error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)

        if den == 0:
            return "Error: Cannot divide by zero."

        return f"The result of the division is {num / den:.2f}"
    except ValueError:
        return "Error: Please enter numeric values only."

