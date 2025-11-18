# Define the annual interest rate as a constant
ANNUAL_INTEREST_RATE = 0.05
MONTHS_IN_YEAR = 12

# Use a try-except block to handle potential non-numeric input gracefully
try:
    # 1. User Input for Financial Details
    # Prompt for income and convert input to a floating-point number (float)
    income_str = input("Enter your monthly income: ")
    monthly_income = float(income_str)

    # Prompt for expenses and convert input to a floating-point number (float)
    expenses_str = input("Enter your total monthly expenses: ")
    monthly_expenses = float(expenses_str)

    # 2. Calculate Monthly Savings
    monthly_savings = monthly_income - monthly_expenses

    # 3. Project Annual Savings
    # Calculation steps:
    # 1. Total savings over 12 months (without interest)
    annual_savings_base = monthly_savings * MONTHS_IN_YEAR

    # 2. Calculate simple interest earned (Base * Rate)
    interest_earned = annual_savings_base * ANNUAL_INTEREST_RATE

    # 3. Projected total savings (Base + Interest)
    projected_savings = annual_savings_base + interest_earned

    # 4. Output Results
    # Display the monthly savings
    print(f"Your monthly savings are ${monthly_savings:,.0f}.")

    # Display the projected annual savings, formatted to two decimal places
    print(f"Projected savings after one year, with interest, is: ${projected_savings:,.2f}.")

except ValueError:
    # Handle cases where the user inputs text instead of numbers
    print("Invalid input. Please enter numerical values for income and expenses.")

