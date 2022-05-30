

from models.Book import Book

class Product:
    def __init__(self, product_id: int, book: Book, price: int, amount: int):
        self.id = product_id
        self.book = book 
        self.price = price
        self.amount = amount