from library import Library
from book import Book
from member import Member

library = Library()
library.load_data()

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. View All Books")
    print("7. View All Members")
    print("8. Save Data")
    print("9. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        year = input("Year: ")

        library.add_book(Book(title, author, isbn, year))
        print("Book added successfully")

    elif choice == "2":

        name = input("Member Name: ")
        member_id = input("Member ID: ")

        library.register_member(Member(name, member_id))
        print("Member registered")

    elif choice == "3":

        member_id = input("Member ID: ")
        isbn = input("ISBN: ")

        library.borrow_book(member_id, isbn)

    elif choice == "4":

        member_id = input("Member ID: ")
        isbn = input("ISBN: ")

        library.return_book(member_id, isbn)

    elif choice == "5":

        keyword = input("Search: ")

        results = library.find_book(keyword)

        for book in results:
            print(
                f"{book.title} | {book.author} | {book.isbn}"
            )

    elif choice == "6":

        for book in library.books.values():
            print(
                f"{book.title} | {book.author} | {book.isbn}"
            )

    elif choice == "7":

        for member in library.members.values():
            print(
                f"{member.name} | {member.member_id}"
            )

    elif choice == "8":

        library.save_data()
        print("Data saved")

    elif choice == "9":

        library.save_data()
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")
