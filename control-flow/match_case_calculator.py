# Define a central function to handle the calculation and output
def run_calculator():
    """
    Prompts the user for two numbers and an operation, then performs the
    calculation using a match-case statement.
    """
    try:
        # 1. Prompt for User Input and convert to float (to handle decimals)
        num1_str = input("Enter the first number: ")
        num1 = float(num1_str)

        num2_str = input("Enter the second number: ")
        num2 = float(num2_str)

        operation = input("Choose the operation (+, -, *, /): ")
        
        result = None

        # 2. Perform the Calculation Using Match Case
        match operation:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '*':
                result = num1 * num2
            case '/':
                # Ensure to handle the division by zero case gracefully
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Cannot divide by zero.")
                    return # Exit the function after printing the error
            case _:
                # Default case for invalid operation input
                print(f"Invalid operation: {operation}. Please use +, -, *, or /.")
                return

        # 3. Output the Result
        # This only runs if a calculation was successful (i.e., not a division by zero error)
        if result is not None:
            # Display the result, formatted to two decimal places for clarity
            print(f"The result is {result:.2f}")

    except ValueError:
        # Handle cases where the user inputs non-numeric characters for the numbers
        print("Invalid input. Please enter valid numerical values for the numbers.")

# Run the calculator function
run_calculator()