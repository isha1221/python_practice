# 6. Problem: Library System with Composition
# Prompt:
# Design two classes: Book and Library.
# Book has title and author.
# Library contains a list of books with methods:
#     add_book(book)
#     remove_book(book)
#     list_books() – prints all books' titles and authors

class book():
    def __init__(self,title,author):
        pass
    
class library():
    def __init__(self):
        pass
    def add_book(self,book):
           self.book=book
           
    def remove_book(self,book):
        self.book=book
        
    def list_books(self):
        self.book            