def generate_table():
    """
    Prompts the user for a number and prints its multiplication table from 1 to 10
    using a for loop.
    """
    try:
        # 1. Prompt User for a Number
        number_str = input("Enter a number to see its multiplication table: ")
        # Convert the input to an integer for calculation
        number = int(number_str)

        # 2. Generate and Print the Multiplication Table
        # The range(1, 11) generates numbers 1, 2, 3, ..., up to 10 (11 is exclusive).
        for i in range(1, 11):
            # Calculate the product
            product = number * i
            
            # Print the result in the required format: "X * Y = Z"
            print(f"{number} * {i} = {product}")
            
    except ValueError:
        # Handle cases where the user inputs non-numeric characters
        print("Invalid input. Please enter a whole number.")

# Run the function to execute the script logic
generate_table()