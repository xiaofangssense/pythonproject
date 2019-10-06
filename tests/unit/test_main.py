import unittest
from unittest.mock import MagicMock, Mock

from flask import json

from app.database import DB
from app.entities.product import Product
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

        self.assertAlmostEqual({"products": [{"product_code": "foo"}]}, products)
