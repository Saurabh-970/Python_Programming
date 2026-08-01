import json

class Book:

    def __init__(self, book_id, name, author):
        self.book_id = book_id
        self.name = name
        self.author = author

        self.available = True
        self.issued_to = None

#----------------------------------------------------------------------------------#
    
    def display(self):

        status = "Available" if self.available else "Issued"

        print("=" * 45)
        print(f"Book ID   : {self.book_id}")
        print(f"Book Name : {self.name}")
        print(f"Author    : {self.author}")
        print(f"Status    : {status}")

        if self.issued_to:
            print(f"Issued To : {self.issued_to}")

        print("=" * 45)

#----------------------------------------------------------------------------------#
    
    def to_dict(self):

        return {
            "book_id": self.book_id,
            "name": self.name,
            "author": self.author,
            "available": self.available,
            "issued_to": self.issued_to
        }



class Library:

    def __init__(self):
        self.books = []

#-------------------------------------------------------------------------------------------------#

    def add_book(self, book):

        for b in self.books:

            if b.book_id == book.book_id:
                print("A book with this Book ID already exists.")
                return

        self.books.append(book)
        self.save_books()

        print("\nBook Added Successfully!\n")
        book.display()

#-------------------------------------------------------------------------------------------------#

    def display_books(self):

        if len(self.books) == 0:
            print("\nNo books available in the library.\n")
            return

        print("\n" + "=" * 45)
        print(f"Total Books : {len(self.books)}")
        print("=" * 45 + "\n")

        for index, book in enumerate(self.books, start=1):
            print(f"Book {index}")
            book.display()

#-------------------------------------------------------------------------------------------------#

    def search_book(self):

        if len(self.books) == 0:
            print("Library is empty")
            return


        print("""
        1. Search by Book ID
        2. Search by Book Name
        """)


        try:
            choice = int(input("Enter search option: "))

        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return



        if choice == 1:

            try:
                book_id = int(input("Enter Book ID: "))

            except ValueError:
                print("Enter numbers only")
                return


            for book in self.books:

                if book.book_id == book_id:

                    print("Book Found")
                    book.display()
                    return


            print("Book not found")



        elif choice == 2:

            name = input("Enter Book Name: ")


            for book in self.books:

                if name.lower() in book.name.lower():

                    print("Book Found")
                    book.display()
                    return


            print("\nBook Found Successfully\n")


        else:
            print("Invalid Option")

#-------------------------------------------------------------------------------------------------#

    def issue_book(self):

        try:
            book_id = int(input("Enter Book ID: "))

        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return



        for book in self.books:

            if book.book_id == book_id:


                if book.available:

                    person = input("Enter borrower name: ")


                    if person.strip() == "":
                        print("Borrower name cannot be empty")
                        return


                    book.available = False
                    book.issued_to = person
                    self.save_books()


                    print(f'\n"{book.name}" has been issued to {person}.\n')
                    return



                else:

                    print("Book already issued")
                    return



        print("Book not found")

#-------------------------------------------------------------------------------------------------#

    def return_book(self):

        try:
            book_id = int(input("Enter Book ID: "))

        except ValueError:
            print("Enter numbers only")
            return


        for book in self.books:

            if book.book_id == book_id:


                if book.available:

                    print("Book is already available")
                    return


                else:

                    book.available = True
                    book.issued_to = None
                    self.save_books()

                    print(f'\n"{book.name}" has been returned successfully.\n')
                    return

        print("---------------")
        print("Book not found")

#-------------------------------------------------------------------------------------------------#

    def remove_book(self):

        self.books.clear()

        if len(self.books) == 0:
            print("Library is empty")
            return

        try:
            book_id = int(input("Enter Book ID to remove: "))

        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return


        for book in self.books:

            if book.book_id == book_id:

                if not book.available:
                    print("Cannot remove an issued book.")
                    return

                self.books.remove(book)
                self.save_books()

                print(f'\n"{book.name}" has been removed from the library.\n')
                return


        print("Book not found.")


#-------------------------------------------------------------------------------------------------#

    def save_books(self):

        data = []

        for book in self.books:
            data.append(book.to_dict())

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

        # print("Books saved successfully.")

#-------------------------------------------------------------------------------------------------#

    def load_books(self):

        try:

            with open("books.json", "r") as file:

                data = json.load(file)

                for item in data:

                    book = Book(
                        item["book_id"],
                        item["name"],
                        item["author"]
                    )

                    book.available = item["available"]
                    book.issued_to = item["issued_to"]

                    self.books.append(book)

        except FileNotFoundError:
            pass

        except json.JSONDecodeError:
            print("books.json is empty or corrupted.")

#-------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------#


def main():

    library = Library()

   
    library.load_books()  # Load books from books.json when program starts

    print("\nLibrary data loaded successfully.\n")

    while True:

        print("""
    =============================
    Library Management System
    =============================

    1. Add Book
    2. Display Books
    3. Search Book
    4. Issue Book
    5. Return Book
    6. Remove Book
    7. Exit

    """)

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue


        if choice == 1:

            try:
                book_id = int(input("Enter Book ID: "))

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue


            name = input("Enter Book Name: ")

            if name.strip() == "":
                print("Book name cannot be empty")
                continue


            author = input("Enter Author Name: ")

            if author.strip() == "":
                print("Author name cannot be empty")
                continue


            book = Book(book_id, name, author)

            library.add_book(book)


        elif choice == 2:

            library.display_books()


        elif choice == 3:

            library.search_book()


        elif choice == 4:

            library.issue_book()


        elif choice == 5:

            library.return_book()


        elif choice == 6:

            library.remove_book()


        elif choice == 7:

            print("""
            ==================================================
            Thank you for using Library Management System.
            Visit Again!
            ==================================================
            """)
            break


        else:

            print("Invalid Choice")


if __name__ == "__main__":
    main()