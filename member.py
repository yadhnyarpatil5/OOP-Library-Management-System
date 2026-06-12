class Member:
    MAX_BOOKS = 5

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, isbn):
        if len(self.borrowed_books) >= self.MAX_BOOKS:
            return False

        self.borrowed_books.append(isbn)
        return True

    def return_book(self, isbn):
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        member = cls(
            data["name"],
            data["member_id"]
        )
        member.borrowed_books = data["borrowed_books"]
        return member
