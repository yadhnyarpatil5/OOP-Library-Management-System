from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True
        self.borrowed_by = None
        self.due_date = None

    def check_out(self, member_id):
        if not self.available:
            return False

        self.available = False
        self.borrowed_by = member_id
        self.due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
        return True

    def return_book(self):
        self.available = True
        self.borrowed_by = None
        self.due_date = None

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "year": self.year,
            "available": self.available,
            "borrowed_by": self.borrowed_by,
            "due_date": self.due_date
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(
            data["title"],
            data["author"],
            data["isbn"],
            data["year"]
        )
        book.available = data["available"]
        book.borrowed_by = data["borrowed_by"]
        book.due_date = data["due_date"]
        return book
