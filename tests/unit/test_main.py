import unittest
from unittest.mock import Mock, patch

import requests
from flask import json

from main import *


class MainFileTestCase(unittest.TestCase):
    """This class will test all methods in main.py file """

    def setUp(self):
        """Define test variables and initialize app."""
        self.stub_db = Mock(DB)
        self.stub_db.init.return_value = None

    def test_hello_world(self):
        hello = hello_world()
        self.assertEqual('Hello Python RESTFUL API World!!!', hello)

    def test_get_product_by_currency_code(self):
        self.stub_db.find.return_value = [{'product_code': 'foo'}]
        products = json.loads(get_product_by_currency_code('foo', self.stub_db.find.return_value))

        self.assertAlmostEqual({'products': [{'product_code': 'foo'}]}, products)

    def test_get_products(self):
        self.stub_db.find.return_value = [{'product_code': 'foo1'}, {'product_code': 'foo2'}]
        products = json.loads(get_products(self.stub_db.find.return_value))
        self.assertAlmostEqual({'products': [{'product_code': 'foo1'}, {'product_code': 'foo2'}]}, products)

    @patch('requests.post')
    def test_add_product_success(self):
        with app.test_client() as c:
            self.stub_db.insert_one.return_value = True
            rv = c.post('/products?db=true',
                        json={'product_code': 'foo', 'amount': 100, 'currency_code': 'foo'
                              })
