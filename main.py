import jwt
import datetime

from flask import jsonify, request, Response
from jwt import ExpiredSignatureError

from config import *
from app.database import DB
from app.entities.product import Product
from bson.json_util import dumps

DB.init()


@app.route('/login')
def get_token():
    # will expire TOKEN_EXPIRED_SECONDS seconds after the clients asked
    expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=app.config['TOKEN_EXPIRED_SECONDS'])
    token = jwt.encode({'exp': expiration_date}, app.config['SECRET_KEY'], algorithm='HS256')
    return token


# Hello Python
@app.route('/')
def hello_world():
    return 'Hello Python RESTFUL API World!!!'


# Get /products/currency/CAD
@app.route('/products/currency/<string:currency_code>')
def get_product_by_currency_code(currency_code, db=None):
    if not app.config['DISABLE_TOKEN'] and not __check_authorization():
        return jsonify({'error': 'Need a valid token.'})
    products = db or DB.find('products', {'currency_code': currency_code})
    return dumps({'products': products})


@app.route('/products')
def get_products(db=None):
    if not app.config['DISABLE_TOKEN'] and not __check_authorization():
        return jsonify({'error': 'Need a valid token.'})
    products = db or DB.find('products', {})
    return dumps({'products': products})


@app.route('/products/<string:product_code>')
def get_product(product_code):
    if not app.config['DISABLE_TOKEN'] and not __check_authorization():
        return jsonify({'error': 'Need a valid token.'})

    products = DB.find('products', {'product_code': product_code})
    return dumps({'products': products})


@app.route('/products', methods=['POST'])
def add_product(db=None):
    if not app.config['DISABLE_TOKEN'] and not __check_authorization():
        return jsonify({'error': 'Need a valid token.'})
    product = __valid_product_object(request.get_json())
    if not product:
        return Response('Missing fields.', 422, mimetype='application/json')

    try:
        db or DB.insert_one('products', product)
        return Response('Insert successfully', 201, mimetype='application/json')
    except ValueError:
        return Response('Failed to insert in DB', 501, mimetype='application/json')

# localhost:5000/products/5d978311afbbf8c790d9db6f
@app.route('/products/<string:pid>', methods=['PUT'])
def replace_product(pid):
    if not app.config['DISABLE_TOKEN'] and not __check_authorization():
        return jsonify({'error': 'Need a valid token.'})
    product = request.get_json()
    product = __valid_product_object(product)
    if not product:
        return Response('Missing fields or product NOT found', 422, mimetype='application/json')
    try:
        DB.find_one_and_replace('products', {'_id': pid}, product)
        return Response('Successfully Updated', 201, mimetype='application/json')
    except ValueError:
        return Response('Some fields may miss.', 422, mimetype='application/json')


@app.route('/products/<string:product_code>', methods=['PATCH'])
def modify_product_fields(product_code):
    if not app.config['DISABLE_TOKEN'] and not __check_authorization():
        return jsonify({'error': 'Need a valid token.'})
    product = request.get_json()
    if not product:
        return Response('Missing parameters', 422, mimetype='application/json')
    try:
        DB.find_one_and_update('products', {'product_code': product_code}, product)
        return Response('Successfully Replaced', 201, mimetype='application/json')
    except ValueError:
        return Response('Failed to replace the product.', 422, mimetype='application/json')


@app.route('/products/<string:product_code>', methods=['DELETE'])
def delete_product(product_code):
    if not app.config['DISABLE_TOKEN'] and not __check_authorization():
        return jsonify({'error': 'Need a valid token.'})
    deleted = DB.delete('products', {'product_code': product_code})
    return Response(deleted, 200, mimetype='application/json')


def __check_authorization():
    token = request.args.get('token')
    if not token:
        return False
    try:
        return jwt.decode(token, app.config['SECRET_KEY'])
    except ExpiredSignatureError:
        print('Signature has expired')
        return False
    except ValueError:
        return False


def __valid_product_object(product_object):
    if ((product_object is not None) and 'product_code' in product_object
            and 'amount' in product_object
            and 'currency_code' in product_object):
        return Product(product_object).json()
    else:
        return False


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=app.config['PORT'])