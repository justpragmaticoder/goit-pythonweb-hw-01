from abc import ABC, abstractmethod

# Class Book, responsible for storing book information (adheres to SRP)
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'


# Interface for the library, defining methods for library operations (adheres to ISP)
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def get_books(self):
        pass


# Class Library, implementing the LibraryInterface (adheres to LSP, OCP)
class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        self.books = [book for book in self.books if book.title != title]

    def get_books(self):
        return self.books


# Class LibraryManager, using LibraryInterface (adheres to DIP)
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str):
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str):
        self.library.remove_book(title)

    def show_books(self):
        books = self.library.get_books()
        if books:
            for book in books:
                print(book)
        else:
            print("No books available in the library.")


# Main function that interacts with the library manager
def main():
    library = Library()
    manager = LibraryManager(library)

    def add_command():
        title = input("Enter book title: ").strip()
        author = input("Enter book author: ").strip()
        year = input("Enter book year: ").strip()
        manager.add_book(title, author, year)

    def remove_command():
        title = input("Enter book title to remove: ").strip()
        manager.remove_book(title)

    def show_command():
        manager.show_books()

    command_dict = {
        "add": add_command,
        "remove": remove_command,
        "show": show_command
    }

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "exit":
            break
        command_dict.get(command, lambda: print("Invalid command. Please try again."))()


if __name__ == "__main__":
    main()