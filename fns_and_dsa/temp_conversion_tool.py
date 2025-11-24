# Define Global Conversion Factors at the top of the script
# These factors are accessible by all functions without the 'global' keyword
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
# Note: F to C formula is (F - 32) * (5/9)
# Note: C to F formula is (C * 9/5) + 32

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.
    Formula: (Fahrenheit - 32) * (5/9)
    """
    # Accessing the global variable FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.
    Formula: (Celsius * 9/5) + 32
    """
    # Accessing the global variable CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Handles user interaction, input validation, and calls the appropriate
    conversion function.
    """
    # 1. Prompt for input
    temp_input = input("Enter the temperature to convert: ")
    unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    try:
        # 2. Input Validation: Check if temperature is numeric
        temperature = float(temp_input)

        result = None
        
        # 3. Perform conversion based on unit
        if unit_input == 'F':
            converted_temp = convert_to_celsius(temperature)
            # Example: 100.0°F is 37.77777777777778°C
            print(f"{temperature}°F is {converted_temp}°C")
            
        elif unit_input == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            # Example: 0.0°C is 32.0°F
            print(f"{temperature}°C is {converted_temp}°F")
            
        else:
            # Handle invalid unit input
            print("Invalid unit. Please enter 'C' or 'F'.")
            
    except ValueError:
        # Handle the required error for non-numeric temperature input
        print("Invalid temperature. Please enter a numeric value.")
        
# Run the main function
if __name__ == "__main__":
    main()