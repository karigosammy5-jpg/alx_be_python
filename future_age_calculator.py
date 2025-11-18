# Define the target year and the number of years from the assumed current year (2023)
TARGET_YEAR = 2050
YEARS_TO_ADD = TARGET_YEAR - 2023  # This calculates 27

# 1. Prompt the user for input and store it.
# The input() function returns a string, so we must convert it to an integer (int).
try:
    current_age_str = input("How old are you? ")
    current_age = int(current_age_str)

    # 2. Calculate the age in the future year (2050)
    future_age = current_age + YEARS_TO_ADD

    # 3. Print the result in the required format
    print(f"In {TARGET_YEAR}, you will be {future_age} years old.")

except ValueError:
    # Handle non-integer input gracefully
    print("Invalid input. Please enter your age as a whole number.")