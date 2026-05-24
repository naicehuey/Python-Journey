# Login System V1 — TXT Storage

A simple command-line login and registration system
built with Python using txt file storage.

## What It Does
- Register a new account with username and password
- Login by matching username and password
- View all registered usernames
- All users saved permanently to a txt file

## What I Learned
- Building a basic authentication system
- Using `and` to check two conditions together —
  username AND password must both match
- Using `_` to hide passwords when displaying usernames
- Using `return` to stop a loop after successful login
- That authentication is just storing credentials
  and checking if they match — the core concept
  behind every login system in the world

## Important Note
Passwords stored as plain text — fine for learning.
Real apps always encrypt passwords using hashing.

## How To Run
```bash
python login_system_v1.py
```