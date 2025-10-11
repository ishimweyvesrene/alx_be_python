# book_class.py

class Book:
    """
    A class that models a book using Python magic methods.
    """

    def __init__(self, title, author, year):
        """Constructor: initialize title, author, and year"""
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __del__(self):
        """Destructor: print a message when object is deleted"""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string output"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation that can recreate the object"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
