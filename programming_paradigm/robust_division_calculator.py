def safe_divide(numerator, denominator):
    """
    Performs division, robustly handling ZeroDivisionError and ValueError.
    """
    try:
        # Step 1: Convert input strings to float (catches ValueError if non-numeric)
        num = float(numerator)
        den = float(denominator)

        # Step 2: Attempt to perform the division (catches ZeroDivisionError if den is 0)
        result = num / den

        # If successful, return the result in the required format
        return f"The result of the division is {result}"

    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."