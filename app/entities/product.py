import datetime


class Product(object):
    def __init__(self, product_obj):
        self.product_code = product_obj['product_code']
        self.amount = product_obj['amount']
        self.currency_code = product_obj['currency_code']

    def json(self):
        return {
            'product_code': self.product_code,
            'amount': self.amount,
            'currency_code': self.currency_code
        }