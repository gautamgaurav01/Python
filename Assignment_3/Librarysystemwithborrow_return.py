class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"You borrowed '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' is already borrowed.")
                    return
        print("Book not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f"You returned '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' is not currently borrowed.")
                    return
        print("Book not found in the library.")


library = Library()
library.add_book(Book("Python Programming", "John Doe"))
library.add_book(Book("Data Structures", "Jane Smith"))

while True:
    print("\n--- Library Menu ---")
    print("1. Display books")
    print("2. Borrow book")
    print("3. Return book")
    print("4. Add book")
    print("5. Exit")

    choice = input("Enter choice: ")

    match choice:
        case "1":
            library.display_books()  # Now matches the method name
        case "2":
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)
        case "3":
            title = input("Enter book title to return: ")
            library.return_book(title)
        case "4":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            library.add_book(Book(title, author))
            print("Book added.")
        case "5":
            print("Exiting system.")
            break
        case _:
            print("Invalid choice. Try again.")
