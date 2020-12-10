from Catalog import *
from User import *
from pdb import set_trace

catalog = Catalog()
# catalog.displayAllBooks()
# set_trace()
librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101')
librarian.catalogAccess(catalog)

book = librarian.addBook('Shoe Dog','Phil Knight', '2015',312)
librarian.addBookItem(book, '123hg','H1B2')
librarian.addBookItem(book, '123hg','H1B4')
librarian.addBookItem(book, '123hg','H1B5')

book = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
librarian.addBookItem(book, '463hg','K1B2')
librarian.addBookItem(book, '463hg','K1B3')
librarian.addBookItem(book, '463hg','K1B4')

# catalog.displayAllBooks()

m1 = Member("Vishal","Bangalore",23,'asljlkj22','std1233')
# m1.availableBooks(catalog)
m1.issueBook(catalog,'Moonwalking with Einstien','463hg',5)
# m1.availableBooks(catalog)
#
# m1.issued_books_details()
# m1.availableBooks(catalog)
# m1.returnBook(catalog,"Moonwalking with Einstien",'463hg','K1B4')
# m1.availableBooks(catalog)
# #
# # set_trace()
#
m2 = Member("Anu","Bangalore",22,'asljlkj23','std1234')
m2.issueBook(catalog,'Moonwalking with Einstien','463hg',0)



print('Issued books', Member.Issued_Books)
#
# catalog.displayAllBooks()
sys1 = System()
sys1.overdue_books()

