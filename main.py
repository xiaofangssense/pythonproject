

import jwt
import datetime

from flask import jsonify, request, Response
from config import *

app.config['SECRET_KEY'] = 'meow'

books = [
    {
        'name': 'Green Eggs',
        'price': 12.8,
        'isbn': 123343
    },
    {
        'name': 'Fallen trees',
        'price': 13.8,
        'isbn': 3543534
    },
    {
        'name': 'Fallen trees another way',
        'price': 13.8,
        'isbn': 3543534
    }
]


@app.route('/login')
def get_token():
    # will expire 100 seconds after the clients asked
    expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
    token = jwt.encode({'exp': expiration_date}, app.config['SECRET_KEY'], algorithm='HS256')
    return token


def valid_book_object(book_object):
    if ('name' in book_object
            and 'price' in book_object
            and 'isbn' in book_object):
        return True
    else:
        return False


# hello
@app.route('/')
def hello_world():
    return 'Hello world!!!'


# Get /books/32423423
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    token = request.args.get('token')
    try:
        jwt.decode(token, app.config['SECRET_KEY'])
        isbn_books = []
        for book in books:
            if book['isbn'] == isbn:
                isbn_books.append(book)
        return jsonify({'books': isbn_books})
    except:
        return jsonify({'error': 'Need a valid token.'})


@app.route('/books')
def get_books():
    token = request.args.get('token')
    try:
        jwt.decode(token, app.config['SECRET_KEY'])
    except:
        return jsonify({'error': 'Need a valid token.'})

    return jsonify({'books': books})


@app.route('/books', methods=['POST'])
def add_book():
    book = request.get_json()
    if valid_book_object(book):
        books.append(book)
        return Response('True', 201, mimetype='application/json')
    else:
        return 'False'


@app.route('/books', methods=['PUT'])
def modify_book():
    book = request.get_json()
    if valid_book_object(book):
        books.append(book)
        return Response('True', 201, mimetype='application/json')
    else:
        return 'False'


app.run(port=5000)
