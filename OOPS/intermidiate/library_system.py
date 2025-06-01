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
        self.title=title
        self.author=author
        pass
    
class library():
    def __init__(self):
        self.books=[]
        pass
    def add_book(self,book):
        self.books.append(book)
        
        return f"You added '{book.title}' by {book.author} to the library."
           
    def remove_book(self,book):
        return self.books.remove(book)
        
    def list_books(self):
        return book            
    
book1=book('abc1','xyz1')
book2=book('abc2','xyz2')
my_lib=library()



print(my_lib.add_book(book1))    