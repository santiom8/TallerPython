# app/library.py
from typing import List

class Book:
    def __init__(self, number: int, name: str, price: float, pages: int, author: str, is_sold: bool):
        self.number = number
        self.name = name
        self.price = price
        self.pages = pages
        self.author = author
        self.is_sold = is_sold

    def __repr__(self):
        return f"{self.name} - {self.pages} pages"

class Library:
    def __init__(self, list_books: List[Book]):
        self.list_books = list_books

    def getList(self) -> List[Book]:
        return self.list_books

    def addNewBook(self, book: Book):
        self.list_books.append(book)

    def deleteBook(self, bookName: str):
        self.list_books = [b for b in self.list_books if b.name != bookName]

    def addPagesBook(self, nameBook: str, pages: int):
        self.list_books = [
            Book(b.number, b.name, b.price, b.pages + pages if b.name == nameBook else b.pages, b.author, b.is_sold)
            for b in self.list_books
        ]

    def sellBook(self, nameBook: str):
        self.list_books = [
            Book(b.number, b.name, b.price, b.pages, b.author, True if b.name == nameBook else b.is_sold)
            for b in self.list_books
        ]
