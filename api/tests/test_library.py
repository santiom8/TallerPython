# tests/test_library.py
import unittest
from app.library import Book, Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.book1 = Book(1, "Book A", 100, 50, "Author 1", False)
        self.book2 = Book(2, "Book B", 150, 70, "Author 2", False)
        self.library = Library([self.book1, self.book2])

    def test_add_new_book(self):
        new_book = Book(3, "Book C", 120, 60, "Author 3", False)
        self.library.addNewBook(new_book)
        self.assertIn(new_book, self.library.getList())
        self.assertEqual(len(self.library.getList()), 3)

    def test_delete_book(self):
        self.library.deleteBook("Book A")
        self.assertEqual(len(self.library.getList()), 1)
        self.assertNotIn(self.book1, self.library.getList())

    def test_add_pages_book(self):
        self.library.addPagesBook("Book A", 30)
        updated_book = self.library.getList()[0]
        self.assertEqual(updated_book.pages, 80)

    def test_sell_book(self):
        self.library.sellBook("Book A")
        updated_book = self.library.getList()[0]
        self.assertTrue(updated_book.is_sold)

    def test_get_list_returns_all_books(self):
        books = self.library.getList()
        self.assertEqual(len(books), 2)
        self.assertIn(self.book1, books)
        self.assertIn(self.book2, books)

if __name__ == "__main__":
    unittest.main()
