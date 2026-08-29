# Microwave — OOP Practice

First Object Oriented Programming project.
A Microwave class that manages state and behavior
of a real world appliance.

## What It Does
- Creates Microwave objects with brand and power rating
- Tracks whether microwave is on or off using a boolean
- Turns on — checks if already on before turning on
- Turns off — checks if already off before turning off
- Runs for a given number of seconds — only if turned on
- Shows current status — ON or OFF
- Prints a clean string representation of the object

## What I Learned

### Core OOP Concepts
- Defining a class with `class Microwave:`
- Using `__init__` to set up object attributes —
  every object gets its own brand, power_rating
  and turned_on state
- Using `self` to refer to the current object —
  `self.brand` means THIS object's brand not
  any other microwave's brand
- Creating multiple instances from one class —
  `smeg` and `bosch` are both Microwaves but
  completely independent objects with their own state

### Methods
- Instance methods — functions that belong to
  the class and always receive `self` as first argument
- `__str__` — controls how the object prints when
  you call `print(smeg)` — professional string
  representation
- Calling methods on objects — `smeg.turn_on()`,
  `smeg.status()`, `smeg.run(50)`

### State Management
- Using a boolean attribute `turned_on` to track
  the current state of the object
- Guard clauses — checking state before every action
  to prevent invalid operations:
  - Can't turn on if already on
  - Can't turn off if already off
  - Can't run if turned off
- That changing `self.turned_on` inside a method
  persists across all method calls on that object

### Type Annotations
- `turned_on: bool` — declaring expected type
- `seconds: int` — declaring parameter type
- That type hints make code more readable and
  professional without affecting how it runs

## Key OOP Concepts Used
- Class definition
- Constructor `__init__`
- Instance attributes
- Instance methods
- State management with boolean
- String representation `__str__`
- Object instantiation
- Type annotations
- Guard clauses

## How To Run
```bash
python microwave.py
```

## Example Output