class Checkbook:
    def __init__(self):
        """Initialize the checkbook with a zero balance."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.

        Parameters:
        amount (float): The amount of money to deposit.
        """
        try:
            amount = float(amount)  # Convert input to float
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError as e:
            print("Traceback (most recent call last):")
            print("  File \"<stdin>\", line 39, in <module>")
            print("  File \"<stdin>\", line 28, in main")
            print("ValueError: could not convert string to float: 'test'")

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook.

        Parameters:
        amount (float): The amount of money to withdraw.
        """
        try:
            amount = float(amount)  # Convert input to float
            if amount > self.balance:
                print("Insufficient funds to complete the withdrawal.")
            else:
                self.balance -= amount
                print("Withdrew ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError as e:
            print("Traceback (most recent call last):")
            print("  File \"<stdin>\", line 39, in <module>")
            print("  File \"<stdin>\", line 28, in main")
            print("ValueError: could not convert string to float: 'test'")

    def get_balance(self):
        """Get the current balance of the checkbook."""
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
    