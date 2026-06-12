import json
import os
from datetime import datetime

from book import Book
from member import Member


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def register_member(self, member):
        self.members[member.member_id] = member

    def find_book(self, keyword):
        results = []

        for book in self.books.values():
            if (
                keyword.lower() in book.title.lower()
                or keyword.lower() in book.author.lower()
                or keyword == book.isbn
            ):
                results.append(book)

        return results

    def borrow_book(self, member_id, isbn):

        if member_id not in self.members:
            print("Member not found")
            return

        if isbn not in self.books:
            print("Book not found")
            return

        member = self.members[member_id]
        book = self.books[isbn]

        if not member.borrow_book(isbn):
            print("Borrow limit reached")
            return

        if book.check_out(member_id):
            print("Book borrowed successfully")
        else:
            print("Book unavailable")

    def return_book(self, member_id, isbn):

        if member_id not in self.members:
            return

        if isbn not in self.books:
            return

        member = self.members[member_id]
        book = self.books[isbn]

        member.return_book(isbn)

        overdue_days = 0

        if book.due_date:
            due = datetime.strptime(book.due_date, "%Y-%m-%d")

            if datetime.now() > due:
                overdue_days = (datetime.now() - due).days

        book.return_book()

        if overdue_days > 0:
            print(f"Returned. Overdue by {overdue_days} days.")
        else:
            print("Book returned successfully.")

    def save_data(self):

        books_data = {
            isbn: book.to_dict()
            for isbn, book in self.books.items()
        }

        members_data = {
            mid: member.to_dict()
            for mid, member in self.members.items()
        }

        with open("books.json", "w") as f:
            json.dump(books_data, f, indent=4)

        with open("members.json", "w") as f:
            json.dump(members_data, f, indent=4)

    def load_data(self):

        if os.path.exists("books.json"):
            with open("books.json", "r") as f:
                books_data = json.load(f)

            for isbn, data in books_data.items():
                self.books[isbn] = Book.from_dict(data)

        if os.path.exists("members.json"):
            with open("members.json", "r") as f:
                members_data = json.load(f)

            for mid, data in members_data.items():
                self.members[mid] = Member.from_dict(data)
