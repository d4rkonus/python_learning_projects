#!/usr/bin/python3

import time

class Library:
    
    @staticmethod
    def add_book(book_list, book):
        book_list.append(book)
        return book_list

    @staticmethod
    def remove_book(book_list, book):
        if book in book_list:
            book_list.remove(book)
            return book

    @staticmethod
    def show_books(book_list):
        return book_list

books = ["1991", "Titanic"]

print("\nLet's check how many books we have:")
time.sleep(2)

for book in Library.show_books(books):
    print(f"- {book}")

Library.add_book(books, "Bowser 320")
Library.add_book(books, "Bee Archive")

time.sleep(2)
print("\nWe have these books available:")
for book in books:
    print(f"- {book}")

removed = Library.remove_book(books, "Bowser 320")

time.sleep(2)
print(f"\nWe removed this book: {removed}")
for book in books:
    print(f"- {book}")
