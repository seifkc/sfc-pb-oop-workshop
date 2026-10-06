"""

You are tasked with developing a system to manage bank accounts.
The system should allow for the following operations:
  Deposit Money: Add a specified amount of money to a bank account.
  Withdraw Money: Subtract a specified amount of money from a bank account,
  but ensure that the account balance does not become negative.
  Check Balance: Retrieve the current balance of a bank account.
See example:

account = BankAccount(100)
account.deposit(50)
print(account.check_balance())  # Prints 150

account.withdraw(30)
print(account.check_balance())  # Prints 120

account.withdraw(100)
print(account.check_balance())  # Prints 20

account.withdraw(50)  # Prints "Insufficient funds"
print(account.check_balance())  # Prints 20


Once your classes are complete, copy and paste the above example below them in order to test their functionality
"""

class BankAccount:
    def __init__(self, beginning_balance):
        self.balance = beginning_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

account = BankAccount(100)
account.deposit(50)
print(account.check_balance())  # Prints 150

account.withdraw(30)
print(account.check_balance())  # Prints 120

account.withdraw(100)
print(account.check_balance())  # Prints 20

account.withdraw(50)  # Prints "Insufficient funds"
print(account.check_balance())  # Prints 20
