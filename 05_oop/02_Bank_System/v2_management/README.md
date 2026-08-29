# Bank Account Management V2 — OOP

An upgraded bank account system built with Python
using inheritance and polymorphism.
Five different account types each with unique rules.

## Account Types

### BankAccount (Base Class)
The parent class all accounts inherit from.
- Deposit with minimum amount validation
- Withdraw with balance validation
- Shared logic used by all child classes

### SavingsAccount
Inherits from BankAccount.
- Adds interest rate attribute
- `apply_interest()` — calculates and adds
  interest to balance automatically

### CurrentAccount
Inherits from BankAccount.
- Adds overdraft limit — can go below zero
- Overrides `withdraw()` — allows withdrawal
  up to balance plus overdraft limit

### FixedDepositAccount
Inherits from BankAccount.
- Locked for 1 year from creation date
- Uses `datetime` to track lock period
- Overrides `withdraw()` — blocked if locked
- Calls `super().withdraw()` when unlocked

### MonthlyLimitSavings
Inherits from BankAccount.
- Limits withdrawals to 3 per month
- Tracks current month and resets counter
  automatically when month changes
- Overrides `withdraw()` — blocks when limit reached

### LowBalanceFeeAccount
Inherits from BankAccount.
- Charges $5 fee after any withdrawal that
  leaves balance below $50
- Overrides `withdraw()` — calls parent then
  checks balance for fee

## What I Learned

### Inheritance
- All account types inherit from `BankAccount`
  using `super().__init__(owner, balance)`
- Writing shared logic once in the parent —
  all children get deposit and withdraw for free
- Adding new attributes in child `__init__`
  on top of parent attributes

### Polymorphism
- `withdraw()` exists on all account types
  but behaves differently for each one —
  CurrentAccount allows overdraft, FixedDeposit
  blocks when locked, MonthlyLimit blocks
  after 3 withdrawals
- Python automatically calls the right version
  based on which type of account it is

### super()
- `super().__init__()` — calls parent constructor
  to set up shared attributes before adding new ones
- `super().withdraw()` — calls parent withdraw
  logic from inside child's overridden method
  instead of rewriting it

### datetime
- `datetime.now()` — getting current date and time
- `timedelta(days=365)` — adding time to a date
- `datetime.now().month` — getting just the month
  number for monthly tracking

### Default Parameters
- `balance=0` in `__init__` — account starts
  at zero if no balance given
- `monthly_limit=3` — default limit but can
  be changed when creating the object

## How To Run
```bash
python bank_account_management.py
```

## Example Output