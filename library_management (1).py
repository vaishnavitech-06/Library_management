class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.available=True
    def display(self):       
        print("Title:",self.title)
        print("Author:",self.author)
        print("available:",self.available)
class Library: 
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def show_books(self):
        for book in self.books:
            book.display()
    def issue_book(self,title):
        for book in self.books:
            if book.title==title and book.available:
                book.available=False
                print("Book issued successfully.")
                return
        print("Sorry, the book is not found in the library.")
    def return_book(self,title):
        for book in self.books:
            if book.title==title:
                book.available=True
                print("Book returned successfully.")
                return
        print("Sorry, the book is not found in the library.")

book1 =Book("wings of fire","APJ Abdul Kalam")
book2 =Book("2state","Chetan Bhagat") 

library =Library()
library.add_book(book1)
library.add_book(book2)

library.show_books()
library.issue_book("python programming")



