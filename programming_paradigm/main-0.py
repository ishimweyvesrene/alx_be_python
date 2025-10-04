import sys
from bank_account import BankAccount

BALANCE_FILE = "balance.txt"

def load_balance():
    """Load balance from file, or start at 0 if file does not exist."""
    try:
        with open(BALANCE_FILE, "r") as f:
            return float(f.read().strip())
    except FileNotFoundError:
        return 0.0

def save_balance(balance):
    """Save the balance to a file."""
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))

def main():
    # Load existing balance
    initial_balance = load_balance()
    account = BankAccount(initial_balance)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_input = sys.argv[1]
    parts = command_input.split(':')
    command = parts[0]
    amount = float(parts[1]) if len(parts) > 1 else None

    try:
        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount}")
        elif command == "withdraw" and amount is not None:
            account.withdraw(amount)
            print(f"Withdrew: ${amount}")
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command or missing amount.")

        # Save updated balance after any change
        save_balance(account.get_balance())

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
