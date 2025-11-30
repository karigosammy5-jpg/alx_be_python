class Book:
    """Represents a single book with a title, author, and availability status."""
    
    def __init__(self, title: str, author: str):
        # Public attributes (accessible directly)
        self.title = title
        self.author = author
        
        # Private attribute (internal state for availability)
        self._is_checked_out = False

    def check_out(self) -> bool:
        """Marks the book as checked out (unavailable)."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self) -> bool:
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self) -> bool:
        """Returns True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    """Manages a collection of Book objects."""

    def __init__(self):
        # Private list to store Book instances (encapsulation)
        self._books = []

    def add_book(self, book: Book):
        """Adds a Book object to the library's collection."""
        self._books.append(book)
        print(f"Book added: {book.title} by {book.author}")

    def check_out_book(self, title: str):
        """Finds a book by title and checks it out if available."""
        title = title.strip()
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {title}")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book not found: {title}")

    def return_book(self, title: str):
        """Finds a book by title and marks it as returned."""
        title = title.strip()
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {title}")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Book not found: {title}")

    def list_available_books(self):
        """Prints the title and author of all books currently available (not checked out)."""
        available = False
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                available = True
        
        if not available:
            print("No books are currently available.")