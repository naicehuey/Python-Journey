class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
        self.reservation_queue = []

    def __str__(self):
        return f"""
            Title: {self.title}
            Author: {self.author}
            Available: {self.available}
        """

    def display(self):
        print(f"""
            ID: {self.book_id}
            Title: {self.title}
            Author: {self.author}
            Availability: {self.available}
        """)

    def mark_as_borrowed(self):
        if self.available:
            self.available = False

    def mark_as_returned(self):
        if not self.available:
            self.available = True

    def add_reservation(self, member):
        if member not in self.reservation_queue:
            self.reservation_queue.append(member)

    def get_next_reservation(self):
        if self.reservation_queue:
            return self.reservation_queue.pop(0)

        return None


class Member:
    def __init__(self, member_id, name, email, contact):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.contact = contact
        self.borrowed_books = []

    def display(self):
        print(f"""
            Member ID: {self.member_id}
            Name: {self.name}
            Email: {self.email}
            Borrowed Books:
                {"\n".join(str(book) for book in self.borrowed_books)}
        """)

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)

    def count_borrowed_books(self):
        return len(self.borrowed_books)

    def get_borrowing_limit(self):
        return 2


class StudentMember(Member):

    def __init__(self, member_id, name, email, contact, student_status):
        super().__init__(member_id, name, email, contact)
        self.student_status = student_status

    def get_borrowing_limit(self):
        return 3

class LibraryMember(Member):

    def __init__(self, member_id, name, email, contact, library_member_status):
        super().__init__(member_id, name, email, contact)
        self.library_member_status = library_member_status

    def get_borrowing_limit(self):
        return 5

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            book.display()

    def find_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                return book

        return None

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
            
        return None

    def get_member_and_book(self, member_id, title):
        member = self.find_member(member_id)
        book = self.find_book(title)

        return member, book

    def borrow_book(self, member_id, title):
        member, book = self.get_member_and_book(member_id, title)

        if not member:
            return "Member not found"

        if not book:
            return "Book not found"

        limit_message = self.check_borrowing_limit(member)

        if limit_message:
            return limit_message

        if not book.available:
            book.add_reservation(member)
            return f"Book already borrowed. {member.name} has been added to the reservation queue."

        book.mark_as_borrowed()
        member.borrow_book(book)

        return f"{member.name} has successfully borrowed the book"

    def return_book(self, member_id, title):
        member, book = self.get_member_and_book(member_id, title)

        if not member:
            return "Member not found"

        if not book:
            return "Book not found"

        if book not in member.borrowed_books:
            return f"{member.name} did not borrow this book"

        member.return_book(book)

        next_member = book.get_next_reservation()

        if next_member:
            book.mark_as_borrowed()
            next_member.borrow_book(book)

            return f"Book returned and transferred to the {next_member.name}"

        book.mark_as_returned()

        return f"{member.name} has successfully returned the book."

    def register_member(self, member):
        self.members.append(member)

    def check_borrowing_limit(self, member):
        if len(member.borrowed_books) >= member.get_borrowing_limit():
            return f"{member.name} has reached borrowing limit"

        return None

    def display_members(self):
        for member in self.members:
            member.display()

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member

        return None

    def remove_member(self, member_id):
        member = self.find_member(member_id)

        if member:
          self.members.remove(member)
          return member
        
        return None

    def remove_book(self, book_id):
        book = self.find_book_by_id(book_id)

        if book:
           self.books.remove(book)
           return book
        
        return None

    def is_member_registered(self, member_id):
        return self.find_member(member_id) is not None

    def count_available_books(self):
        count = 0

        for book in self.books:
            if book.available:
                count += 1

        return count

    def count_member_books(self, member_id):
        member = self.find_member(member_id)

        if not member:
            return None

        return member.count_borrowed_books()


# -------------------------
# Creating objects
# -------------------------

book1 = Book(
    1,
    "The Return Of Author",
    "James Makeke"
)

book2 = Book(
    2,
    "Jack The Giant Slayer",
    "Mark Herny"
)

book3 = Book(
    3,
    "Assemble",
    "Marlian Settle"
)

book4 = Book(
    4,
    "Infinity Wars",
    "Herny Lee"
)


book5 = Book(
    5,
    "Age Of Ultron",
    "Jane Mennis"
)

book6 = Book(
    6,
    "Doomsday",
    "Mary Herny"
)


member1 = Member(
    1,
    "John Kasimba",
    "Yatowa@983.com",
    94837521
)

member2 = Member(
    2,
    "Mary Banda",
    "mary@example.com",
    987564634
)

student1 = StudentMember(
    3,
    "Peter Parker",
    "Peter@Jarvis.com",
    9749573462,
    "Active"
)

library_member1 =LibraryMember(
    4,
    "Bruce Wayne",
    "Bruce@Waynema",
    8946836245,
    "Premium"
)

library = Library()


# -------------------------
# Adding books and members
# -------------------------

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)

library.register_member(member1)

library.register_member(member2)

library.register_member(student1)

library.register_member(library_member1)


# -------------------------
# Testing
# -------------------------

print(library.borrow_book(1, "The Return"))

print(library.borrow_book(2, "The Return"))

print(library.borrow_book(3, "Assemble"))

print(library.borrow_book(3, "Doomsday"))

print(library.borrow_book(3, "Age Of Ultron"))

print(library.borrow_book(3, "Jack The Giant"))

print(library.borrow_book(4, "Infinity Wars"))

library.display_books()

print(f"Available books: {library.count_available_books()}")

print(f"{member1.name} has borrowed: {library.count_member_books(1)} book(s)")

print(library.return_book(1, "The Return"))

member1.display()

member2.display()

print(f"{student1.name} can only borrow{student1.get_borrowing_limit()} books")
print(f"{library_member1.name} can only borrow {library_member1.get_borrowing_limit()} books")