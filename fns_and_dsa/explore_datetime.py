from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains the current date and time and prints it in the format YYYY-MM-DD HH:MM:SS.
    
    The function returns the current datetime object so it can be used by other functions.
    """
    # Part 1: Display the Current Date and Time
    current_date = datetime.now()
    
    # Format and print the current date and time
    # The format string is "%Y-%m-%d %H:%M:%S"
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    
    # Return the raw datetime object for reuse in the next function
    return current_date

def calculate_future_date(current_date):
    """
    Prompts the user for a number of days and calculates the future date.
    
    Args:
        current_date (datetime): The datetime object representing the current time.
    """
    # Part 2: Calculate a Future Date
    
    try:
        # Prompt the user for the number of days to add
        days_to_add_str = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_to_add_str)
        
        # Calculate the future date using timedelta
        # timedelta represents a duration (days, seconds, etc.)
        future_date = current_date + timedelta(days=days_to_add)
        
        # Print the future date in the required format: YYYY-MM-DD
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
        
        # Return the future date object (optional, but good practice)
        return future_date

    except ValueError:
        print("Invalid input. Please enter a whole number for the number of days.")


# Execute the functions when the script is run
if __name__ == "__main__":
    # Get the current date and time from Part 1
    current_date_obj = display_current_datetime()
    
    # Pass the current date object to Part 2 for calculation
    calculate_future_date(current_date_obj)