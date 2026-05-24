# Login System V2 — JSON Storage

A rebuilt login system with real world security
features built with Python and JSON storage.

## What It Does
- Register with username and password validation
- Login with attempt limiting — locks after 3 fails
- Validates password length — minimum 8 characters
- Validates empty fields before processing
- Shows remaining attempts after each failure
- All users saved permanently using JSON

## What I Learned
- Limiting login attempts with a countdown —
  `while attempt > 0` and `attempt -= 1`
- Using two separate boolean flags —
  `found_user` and `correct_password`
- Enforcing password rules with `len(password) < 8`
- Using `continue` to skip back to top of loop
- That real login systems always have attempt limits,
  password rules and specific error messages

## Growth From V1
V1 had no validation or limits.
V2 adds password rules, attempt limiting
and JSON storage — same idea at professional level.

## How To Run
```bash
python login_system_v2.py
```