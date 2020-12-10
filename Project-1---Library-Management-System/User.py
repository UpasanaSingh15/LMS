from Catalog import Catalog
from datetime import datetime, timedelta


class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        

class Member(User):

    Issued_Books = []

    def __init__(self, name, location, age, aadhar_id, student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.limit = 5
        self.issued_books = {}

    def searchByName(self,catalog ,name):
        return catalog.searchByName(name)

    def searchByAuthor(self, catalog, name):
        return catalog.searchByAuthor(name)

    def availableBooks(self, catalog):
        catalog.displayAllBooks()

    def issueBook(self, catalog, name, isbn, days=10):
        if self.limit:
            catalog.removeBookItem(name, isbn)
            book_issued = {name: {'returned_date': datetime.now() + timedelta(days), 'fine': 0}}
            self.issued_books.update(book_issued)
            Member.all_books_issued(self.name, book_issued)
            self.limit -= 1
        else:
            print('Already 5 Books are Issued!!')

    def returnBook(self, catalog, name, isbn, rack):
        book = catalog.searchByName(name)
        catalog.addBookItem(book, isbn, rack)

    @classmethod
    def all_books_issued(cls, name, book):
        cls.Issued_Books.append({name:book})

    def issued_books_details(self):
        print('*********Issued books details***************')
        for book_name, book_detail in self.issued_books.items():
            print('Book Name: ', book_name)
            print('Returned Date: ', book_detail['returned_date'].strftime('%d-%m-%y %H:%M:%S'))

    def __repr__(self):
        return self.name + '_' + self.location + '_' + self.student_id


class Librarian(User):

    def __init__(self, name, location, age, aadhar_id, emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id

    def catalogAccess(self, catalog):
        self.catalog = catalog

    def addBook(self, name, author, publish_date, pages):
        return self.catalog.addBook(name, author, publish_date, pages)

    def addBookItem(self, book, isbn, rack):
        self.catalog.addBookItem(book, isbn, rack)

    def removeBook(self, name):
        self.catalog.removeBook(name)

    def removeBookItemFromCatalog(self, name, isbn):
        self.catalog.removeBookItem(name, isbn)

    def __repr__(self):
        return self.name + self.location + self.emp_id


class System:

    def __init__(self):
        self.members = None

    @property
    def fine_amount(self):
        return 100

    def get_members_issued_books(self):
        self.members = Member.Issued_Books

    def overdue_books(self):
        self.get_members_issued_books()
        for books in self.members:
            for member_name,issued_book in books.items():
                for book_name,book_details in issued_book.items():
                    days_pending = book_details['returned_date'] - datetime.now()
                    if days_pending.days <= 0:
                        book_details['fine'] = self.fine_amount
                        self.notify(member_name,book_name, self.fine_amount)

    def notify(self, user_name, book_name, fine_amount):
        print(f'Hey {user_name}! {book_name} book have not been returned before the due date.')
        print(f'Kindly return the book and pay the fine amount of rupees {fine_amount} or else account will be blocked.')