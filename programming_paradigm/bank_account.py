# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Remove money from the account if sufficient funds exist."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        elif amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False  # not enough funds

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
