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

# hello
@app.route('/')
def hello_world():
    return 'Hello Python World!!!'


# Get /products/CAD
@app.route('/products/<string:currency_code>')
def get_product_by_currency_code(currency_code):
    if not __check_authorization():
        return jsonify({'error': 'Need a valid token.'})

    currency_code_products = []
    for product in products:
        if product['currency_code'] == currency_code:
            currency_code_products.append(product)
    return jsonify({'products': currency_code_products})


@app.route('/products')
def get_products():
    if not __check_authorization():
        return jsonify({'error': 'Need a valid token.'})

    return jsonify({'products': products})


@app.route('/products', methods=['POST'])
def add_product():
    if not __check_authorization():
        return jsonify({'error': 'Need a valid token.'})
    product = request.get_json()
    if __valid_product_object(product):
        products.append(product)
        return Response('True', 201, mimetype='application/json')
    else:
        return 'False'


@app.route('/products/<string:product_code>', methods=['PUT'])
def modify_product():
    if not __check_authorization():
        return jsonify({'error': 'Need a valid token.'})
    product = request.get_json()
    if __valid_product_object(product):
        for i, prod in enumerate(products):
            if prod['product_code'] == product['product_code']:
                products[i] = product
        return Response('True', 201, mimetype='application/json')
    else:
        return 'False'


@app.route('/products/modify/<string:product_code>', methods=['PATCH'])
def modify_product_fields():
    if not __check_authorization():
        return jsonify({'error': 'Need a valid token.'})
    product = request.get_json()
    for i, prod in enumerate(products):
        if prod['product_code'] == product['product_code']:
            if product['amount']:
                products[i]['amount'] = product['amount']
            if product['currency_code']:
                products[i]['currency_code'] = product['currency_code']
            return Response('True', 201, mimetype='application/json')
    else:
        return Response('False', 400, mimetype='application/json')


@app.route('/products/<string:product_code>', methods=['DELETE'])
def delete_product(product_code):
    if not __check_authorization():
        return jsonify({'error': 'Need a valid token.'})
    for i, prod in enumerate(products):
        if prod['product_code'] == product_code:
            del products[i]
            return Response('Deleted', 204, mimetype='application/json')

    return Response('Not found', 404, mimetype='application/json')


def __check_authorization():
    token = request.args.get('token')
    try:
        return jwt.decode(token, app.config['SECRET_KEY'])
    except:
        return False


def __valid_product_object(product_object):
    if ('product_code' in product_object
            and 'amount' in product_object
            and 'currency_code' in product_object):
        return True
    else:
        return False


app.run(port=5000, debug=True)

