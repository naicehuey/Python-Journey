# Mobile Money App — TNM / Airtel Money

A command-line mobile money application built
with Python and JSON storage. Inspired by real
mobile money services in Malawi.

## What It Does
- Register a new account with username and PIN
- Login with username and PIN authentication
- Withdraw money with balance validation
- Deposit money into your account
- Delete your account permanently
- Logout and return to main menu
- All accounts and balances saved permanently
  using JSON — data persists between sessions

## What I Learned
- Using `global` to share a variable across
  multiple functions — `logged_in`
- Returning `True` or `False` from a function
  to signal success or failure to the caller
- Using a nested `while` loop — action menu
  only appears after successful login
- Using `accounts.remove(logged_in)` to delete
  the exact logged in account from the list
- Using `-=` and `+=` to update balance in place
  instead of creating a new variable
- Saving after every change — deposit, withdraw
  and delete all call `save_account()` immediately
- Checking balance before allowing withdrawal —
  defensive programming
- Building a proper logout that clears `logged_in`
  and returns to main menu
- That a variable can point to an item inside a list —
  changing `logged_in` automatically updates
  the accounts list because they share the same
  place in memory

## How It Works — Login Flow
Main Menu
↓
Register → creates account → back to main menu
↓
Login → finds matching account → stores in logged_in
↓
If login successful → action menu appears
↓
Withdraw / Deposit / Delete / Logout
↓
Logout or Delete → back to main menu

## How To Run
```bash
python mobile_money.py
```

## Example
==============================
Main Menu

New Account
Login
Exit
Choose Option: 2
==============================
Login Account
==============================
Username: naicehuey
What is your pin: 1234
==============================
Login Successful
Do you want to withdraw
Do you want to deposit
Delete account
Logout
Enter your Option: 2
==============================
Deposit
==============================
How much you wanna deposit: 5000
==============================
Balance: 5000