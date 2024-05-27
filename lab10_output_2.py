#!/usr/bin/env python
# coding: utf-8

# In[1]:


class LibraryBook:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

class LibraryBookInfo:
    def __init__(self, library_book):
        self.library_book = library_book

    def get_book_info(self):
        return {
            "Title": self.library_book.title,
            "Author": self.library_book.author,
            "Publication Year": self.library_book.publication_year,
            "Checked Out": self.library_book.is_checked_out
        }

    def check_book_condition(self):
       
        return "Good"  

book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book_info = LibraryBookInfo(book)

print(book.check_out())
print(book.check_out())
print(book.return_book())
print(book.return_book())
print(book_info.get_book_info())
print(book_info.check_book_condition())


# In[ ]:




