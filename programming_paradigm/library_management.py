class Book:
    """Represents a book in the library."""

    def __init__(self, title, author):
        """Initialize a book with a title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out


class Library:
    """Represents a library that manages a collection of books."""

    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self._books = []  # private list of Book instances

    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by title.
        If the book is found and available, mark it as checked out.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """
        Return a book by title.
        If the book is found and was checked out, mark it as available.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """Print all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
