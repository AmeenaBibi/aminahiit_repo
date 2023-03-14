class Book:
    def __init__(self, title, author, isbn, available : bool):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def checkout(self):
        if self.available:
            self.available = False
        else:
            print('Book is not available')

    def checking(self):
        if self.available == False:
            self.available = True
        else:
            print('Book was not given out')

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}'
    
class Library:
    def __init__(self):
        self.library = []

    def addBook(self, book : Book):
        self.library.append(book) 

    def addBooks(self, books : list):
        for book in books:
            self.library.append(book)

    def remove(self, book : Book):
        self.library.remove(book)

    def displayAvailableBooks(self):
        for book in self.library:
            if book.available == True:
                print(book)

    def searchBook(self, title, author):
        for book in self.library:
            if(book.title == title) & (book.author == author):
                return book
        else:
            print('Could not find the book in the library')

book1 = Book('Harry Porter', 'John Brown', 'IHSH193333', True)
book2 = Book('Things Fall Apart', 'Chinwe Achebe', '1110002232', True)
book3 = Book('Americana', 'Chimamanda', 'HDHDG112', True)
book4 = Book('Lord Of The Rings', 'John Brown', 'WITH111233', True)

nationalLibrary = Library()
nationalLibrary.addBook(book1)
nationalLibrary.addBooks([book2, book3, book4])

nationalLibrary.displayAvailableBooks()