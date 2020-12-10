from Book import Book


class Catalog:

    def __init__(self):
        self.different_book_count = 0
        self.books = []

    def addBook(self, name, author, publish_date, pages):
        b = Book(name, author, publish_date, pages)
        self.different_book_count += 1
        self.books.append(b) # each obj can store 1 or more copies of book
        return b

    def addBookItem(self, book, isbn, rack):
        book.addBookItem(isbn, rack)

    def searchByName(self,name):
        for book in self.books:
            if name.strip() == book.name:
                return book
    
    def searchByAuthor(self,author):
        for book in self.books: # newly defined
            if author.strip() == book.author:
                return book

    def displayAllBooks(self):

        if not self.different_book_count:
            print('Sorry No books are available!!!')
            return

        print('Different Book Count', self.different_book_count)
        c = 0
        for book in self.books:
            c += book.total_count
            book.printBook()
        
        print('Total Book Present in Catalog:', c)

    def removeBook(self,name):
        book = self.searchByName(name)
        self.books.remove(book)
        del book
        self.different_book_count -= 1
        print(f'<<{name}>> Book is removed from the catalog successfully!!')

    def removeBookItem(self,name,isbn):
        book = self.searchByName(name)
        book_item = book.searchBookItem(isbn)
        book.removeBookItem(book_item)

    def __repr__(self):
        print(self.books)