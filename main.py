# Нужные билбиотеки для работы
from flask import Flask, jsonify, request
from models.Book import Book
from models.Product import Product


# Инициализируем Flask
app = Flask(__name__)

# Переменные для псевдо БД
userBooks = []

marketProducts = [
    Product(0, Book("Философия Java", "Брюс Эккель"), 100, 3),
    Product(1, Book("Думай медленно... Решай быстро", "Думай медленно... Решай быстро"), 70, 2)
]

# Функции 

def getAccountBooks():
    """ Используется для того чтобы привести значения из списка в json вид """
    books = []
    for i in userBooks:
        books.append({
            "name": i.name,
            "author": i.author
        })
    return books 


def getMarketProducts():
    """ Используется для того чтобы привести значения из списка в json вид """
    products = []
    for i in marketProducts:
        products.append({
            "id": i.id,
            "book": {
                "name": i.book.name,
                "author": i.book.author
            },
            "price": i.price,
            "amount": i.amount
        })
    return products

# Обработчики

@app.route('/account', methods=['GET'])
def getAccountRoute():
    return jsonify({
        "balance": 100,
        "books": getAccountBooks()
    })


@app.route('/market', methods=['GET'])
def getMarket():
    return jsonify(getMarketProducts())


@app.route('/market/deal', methods=['GET'])
def postMarketDeal():
    content = request.json
    product_id = content["id"]
    product_amount = content["amount"]


if __name__ == '__main__':
    app.run()