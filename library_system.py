class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def search_book(self, keyword):
        return[book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
    
    def remove_book(self, title):
        self.books = [book for book in self.books if book.title.lower() != title.lower()]