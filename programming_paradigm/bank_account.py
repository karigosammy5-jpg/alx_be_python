class BankAccount:
    """
    Implements a simple bank account with deposit, withdrawal, and balance display.
    Adheres to encapsulation principles by managing the account_balance internally.
    """
    
    def __init__(self, initial_balance=0.0):
        """
        Initializes the bank account with an optional initial balance.
        
        Args:
            initial_balance (float): The starting amount in the account. Defaults to 0.0.
        """
        # Encapsulation: Storing the balance as an instance attribute
        self.account_balance = initial_balance

    def deposit(self, amount: float):
        """
        Adds the specified amount to the account balance.
        
        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount: float) -> bool:
        """
        Deducts the specified amount if the funds are sufficient.
        
        Args:
            amount (float): The amount to withdraw.
            
        Returns:
            bool: True if withdrawal was successful, False otherwise.
        """
        # Check if the withdrawal amount is valid (non-negative) and funds are sufficient
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly, formatted way.
        """
        # Display balance, formatted to two decimal places
        print(f"Current Balance: ${self.account_balance:.2f}")