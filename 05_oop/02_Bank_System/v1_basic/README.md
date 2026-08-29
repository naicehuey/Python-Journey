# Bank Account V1 — OOP Practice

A simple Bank Account class built with Python.
First version — basic deposit, withdraw and summary.

## What It Does
- Creates a bank account with owner and balance
- Deposit money with validation
- Withdraw money with balance and amount validation
- Display account summary

## What I Learned
- Simple class with `__init__`, attributes and methods
- Using `self.balance +=` and `self.balance -=`
  to update balance in place
- Validation before every action —
  invalid amount, insufficient balance
- That object state persists across method calls —
  balance changes from deposit stay when
  withdraw is called next

## How To Run
```bash
python bank_account.py
```

## Example Output
```
Deposited: $500
Withdrawn: $2000
Insufficient balance
====================
Account Holder: James Bond
Balance: $1500
====================
```