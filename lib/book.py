#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title


    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if not isinstance (page_count, int):
            print("page_count must be an integer")
        self._page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        
    
book1 = Book("Hamlet", "432")

print(book1.title)
print(book1.page_count)
book1.turn_page()