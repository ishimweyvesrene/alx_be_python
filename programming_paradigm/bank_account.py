class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
            """ add money to the account."""
            if amount > 0:
                self.__account_balance += amount
            else:
                raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
            """ remove money from the account."""
            if 0 < amount <= self.__account_balance:
                self.__account_balance -= amount
            else:
                raise ValueError("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
            """ return the current balance of the account."""
            print(f"Current Balance: ${self.__account_balance:.2f}")             

    
    def get_balance(self):
        """Return the balance as a number (used for saving)."""
        return self.__account_balance