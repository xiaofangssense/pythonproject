

import jwt
import datetime

from flask import jsonify, request, Response
from config import *

app.config['SECRET_KEY'] = 'meow'

products = [
    {
        'product_code': '192011F110017',
        'amount': 212.8,
        'currency_code': 'CAD'
    },
    {
        'product_code': '182011F110017',
        'amount': 313.8,
        'currency_code': 'USD'
    },
    {
        'product_code': '172011F110017',
        'amount': 513.8,
        'currency_code': 'CAD'
    }
]


@app.route('/login')
def get_token():
    # will expire 100 seconds after the clients asked
    expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
    token = jwt.encode({'exp': expiration_date}, app.config['SECRET_KEY'], algorithm='HS256')
    return token


def valid_product_object(product_object):
    if ('product_code' in product_object
            and 'amount' in product_object
            and 'currency_code' in product_object):
        return True
    else:
        return False


# hello
@app.route('/')
def hello_world():
    return 'Hello Python World!!!'


# Get /products/CAD
@app.route('/products/<string:currency_code>')
def get_product_by_currency_code(currency_code):
    token = request.args.get('token')
    try:
        jwt.decode(token, app.config['SECRET_KEY'])
        currency_code_products = []
        for product in products:
            if product['currency_code'] == currency_code:
                currency_code_products.append(product)
        return jsonify({'products': currency_code_products})
    except:
        return jsonify({'error': 'Need a valid token.'})


@app.route('/products')
def get_products():
    token = request.args.get('token')
    try:
        jwt.decode(token, app.config['SECRET_KEY'])
    except:
        return jsonify({'error': 'Need a valid token.'})

    return jsonify({'products': products})


@app.route('/products', methods=['POST'])
def add_product():
    product = request.get_json()
    if valid_product_object(product):
        products.append(product)
        return Response('True', 201, mimetype='application/json')
    else:
        return 'False'


@app.route('/products', methods=['PUT'])
def modify_product():
    product = request.get_json()
    if valid_product_object(product):
        products.append(product)
        return Response('True', 201, mimetype='application/json')
    else:
        return 'False'


app.run(port=5000)
