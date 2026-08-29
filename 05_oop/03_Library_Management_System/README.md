# Library Management System — OOP

A fully featured command-line library management
system built using Object Oriented Programming
in Python. Uses multiple classes, inheritance
and object relationships.

## Classes

### Book
Represents a library book with availability
tracking and a reservation queue.

**Attributes:**
- `book_id` — unique identifier
- `title` — book title
- `author` — book author
- `available` — True or False
- `reservation_queue` — list of members waiting

**Methods:**
- `mark_as_borrowed()` — sets available to False
- `mark_as_returned()` — sets available to True
- `add_reservation(member)` — adds member to queue
- `get_next_reservation()` — pops first member from queue
- `display()` — prints full book details
- `__str__` — clean string representation

---

### Member
Represents a library member with borrowing
tracking and a borrowing limit.

**Attributes:**
- `member_id` — unique identifier
- `name`, `email`, `contact` — personal details
- `borrowed_books` — list of currently borrowed books

**Methods:**
- `borrow_book(book)` — adds book to borrowed list
- `return_book(book)` — removes book from borrowed list
- `count_borrowed_books()` — returns number borrowed
- `get_borrowing_limit()` — returns 2 (base limit)
- `display()` — prints full member details

---

### StudentMember (inherits from Member)
A student with a higher borrowing limit.

- Inherits all Member attributes and methods
- Adds `student_status` attribute
- Overrides `get_borrowing_limit()` — returns 3

---

### LibraryMember (inherits from Member)
A premium library member with the highest limit.

- Inherits all Member attributes and methods
- Adds `library_member_status` attribute
- Overrides `get_borrowing_limit()` — returns 5

---

### Library
The main system that manages all books and members.

**Methods:**
- `add_book(book)` — adds book to library
- `register_member(member)` — registers a member
- `borrow_book(member_id, title)` — full borrow flow
- `return_book(member_id, title)` — full return flow
- `find_book(title)` — searches by title
- `find_member(member_id)` — searches by ID
- `check_borrowing_limit(member)` — validates limit
- `count_available_books()` — counts available books
- `count_member_books(member_id)` — counts borrowed
- `remove_book(book_id)` — removes a book
- `remove_member(member_id)` — removes a member
- `is_member_registered(member_id)` — checks registration
- `display_books()` — prints all books
- `display_members()` — prints all members

---

## What I Learned

### OOP Concepts
- Building multiple classes that work together
- `__init__` — setting up object state with attributes
- `__str__` — controlling how objects print
- Instance methods that modify object state
- Objects as attributes — `Member` stores
  a list of `Book` objects inside it

### Inheritance
- `StudentMember` and `LibraryMember` both
  inherit from `Member` using `super().__init__()`
- Overriding `get_borrowing_limit()` in each
  subclass — same method name, different behavior
- That inheritance means you write shared code
  once in the parent and specialize in children

### Object Relationships
- `Book` holds a list of `Member` objects
  in its reservation queue
- `Member` holds a list of `Book` objects
  in borrowed_books
- `Library` holds lists of both `Book` and
  `Member` objects
- Objects referencing other objects — not just
  storing strings or numbers but actual objects

### Polymorphism
- `get_borrowing_limit()` exists on all three
  member types but returns different values —
  `Member` returns 2, `StudentMember` returns 3,
  `LibraryMember` returns 5
- `Library.check_borrowing_limit()` calls
  `member.get_borrowing_limit()` without
  knowing which type of member it is —
  Python figures it out automatically

### Queue System
- `reservation_queue` in Book — first in first out
- `list.pop(0)` — removes and returns the first item
- When a book is returned the next person in queue
  automatically gets it — real world library logic!

### Return Values From Methods
- Methods return strings describing what happened
- Caller can print or use the returned message
- Returning `None` when nothing is found —
  consistent pattern across all find methods

## How To Run
```bash
python library_management_system.py
```

## Example Output