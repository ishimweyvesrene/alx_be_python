# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Performs safe division with error handling for invalid input or zero division."""

    try:
        # Try converting inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Try performing division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # Handles case where inputs cannot be converted to numbers
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        # Handles division by zero
        return "Error: Cannot divide by zero."
