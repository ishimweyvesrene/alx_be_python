

# Base Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived Class 1 - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call base class constructor
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived Class 2 - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call base class constructor
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition Class - Library
class Library:
    def __init__(self):
        self.books = []  # holds Book, EBook, or PrintBook instances

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print("\nBooks in Library:")
        for book in self.books:
            print(book)
