def draw_pattern():
    """
    Prompts the user for a size (positive integer N) and prints an N x N
    square pattern of asterisks using a while loop nested with a for loop.
    """
    try:
        # 1. Prompt User for Pattern Size
        size_str = input("Enter the size of the pattern: ")
        size = int(size_str)

        # Input validation: Ensure the size is a positive integer
        if size <= 0:
            print("Please enter a positive integer greater than zero.")
            return

        # Initialize the counter for the outer WHILE loop (Row counter)
        row_count = 0
        
        # 2. Draw the Pattern using nested loops
        # Outer Loop: Controls the rows (runs 'size' times)
        while row_count < size:
            
            # Inner Loop: Controls the columns (prints one row of asterisks)
            # The range(size) iterates from 0 up to (size - 1), which is 'size' times.
            for col_count in range(size):
                # Print an asterisk without advancing to a new line
                print("*", end="")
            
            # After the inner loop finishes (the row is complete), print a newline
            # to move the cursor to the start of the next row.
            print() 
            
            # Increment the row counter to prevent an infinite loop
            row_count += 1
            
    except ValueError:
        # Handle non-integer input gracefully
        print("Invalid input. Please enter a whole number for the size.")

# Run the function to execute the script logic
draw_pattern()