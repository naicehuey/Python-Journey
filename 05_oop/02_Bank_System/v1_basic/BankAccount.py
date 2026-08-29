class BankAccount:

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")

        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")

        elif amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")

    def summary(self):
        print("="*20)
        print(f"Account Holder: {self.owner}")
        print(f"Balance: ${self.balance}")
        print("="*20)

# -------------------------
# Creating object
# -------------------------

account = BankAccount(
    "James Bond",
    3000
    )

# -------------------------
# Testing
# -------------------------

account.deposit(500)
account.withdraw(2000)
account.withdraw(4000)

account.summary()