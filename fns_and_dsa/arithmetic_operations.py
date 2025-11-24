def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations based on the provided parameters.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 
                         'multiply', or 'divide').

    Returns:
        float or str: The result of the operation, or a specific string 
                      if division by zero is attempted.
    """
    
    # Use match-case to handle the different operations efficiently
    match operation:
        case 'add':
            return num1 + num2
        
        case 'subtract':
            return num1 - num2
        
        case 'multiply':
            return num1 * num2
        
        case 'divide':
            # Handle division by zero case as required
            if num2 == 0:
                # Returning a recognizable error message/value
                return "Error: Cannot divide by zero."
            else:
                return num1 / num2
        
        case _:
            # Handle unrecognized operation input
            return f"Error: Invalid operation '{operation}'. Use add, subtract, multiply, or divide."

# Note: You do not need the main.py file here, as it is provided externally 
# for testing your function.