from datetime import datetime, timedelta

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 10:
            print("You cannot deposit less than $10")
        else:
            self.balance += amount
            print(f"Deposited: {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Balance Insufficient")
            print(f"Balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}. Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)
        self.rate = rate

    def apply_interest(self):
        interest = self.balance * self.rate
        self.balance += interest            # ← Fixed!
        print(f"Interest applied! New Balance: {self.balance}")

class CurrentAccount(BankAccount):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. Balance: {self.balance}")
        else:
            print("Overdraft limit exceeded!")

class FixedDepositAccount(BankAccount):
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)
        self.rate = rate
        self.creation_date = datetime.now()
        self.lock_years = 1

    def is_locked(self):
        unlock_date = self.creation_date + timedelta(days=365)
        return datetime.now() < unlock_date

    def withdraw(self, amount):
        if self.is_locked():
            print("Account locked for 1 year. Come back later!")
        else:
            super().withdraw(amount)

class MonthlyLimitSavings(BankAccount):
    def __init__(self, owner, balance, rate, monthly_limit=3):
        super().__init__(owner, balance)
        self.rate = rate
        self.monthly_limit = monthly_limit
        self.withdrawals_this_month = 0
        self.current_month = datetime.now().month

    def withdraw(self, amount):
        now = datetime.now().month       
        if now != self.current_month:
            self.withdrawals_this_month = 0
            self.current_month = now

        if self.withdrawals_this_month >= self.monthly_limit:
            print(f"Monthly limit reached! Only {self.monthly_limit} withdrawals allowed.")
        else:
            super().withdraw(amount)
            self.withdrawals_this_month += 1

class LowBalanceFeeAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance >= amount:      
            super().withdraw(amount)
            if self.balance < 50:
                self.balance -= 5
                print("$5 fee charged for low balance")
        else:
            print("Insufficient balance")

my_account = BankAccount("John", 400)
my_savings = SavingsAccount("Nana", 2090, 0.05)
spender = CurrentAccount("Bob", 500, 200)
monthly = MonthlyLimitSavings("Jane", 1000, 0.02)
test = LowBalanceFeeAccount("Alice", 100)

my_account.deposit(5000)
print(my_account.owner)
print(my_account.balance)

my_savings.deposit(500)
my_savings.apply_interest()
print(my_savings.balance)

my_account.withdraw(600)
my_savings.withdraw(600)
spender.withdraw(600)

monthly.withdraw(100)
monthly.withdraw(100)
monthly.withdraw(100)
monthly.withdraw(100)

test.withdraw(60)
test.withdraw(10)