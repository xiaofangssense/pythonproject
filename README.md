# pythontestproject
## Prequisted
- Make sure the latest official python and pip are installed, could be python 3.7, and pip3
- Make sure MongoDB was installed in your local and also mongo server was run(mongod)
## Getting Started
- Python -m pip install -r requirements.txt
- python main.py
## Run test
- python -m unittest tests
- python -m unittest tests/unit/test_main.py
## Endpoints
- localhost:5000  # Hello world
- [GET] http://localhost:5000/login  # Get the token, could be: `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzAxMjA3NDZ9._uRInw6C2wdTW5AVwqGYSLw-lA0gj_naUcAw0s5z8k0`
- [GET] http://localhost:5000/products?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzAxMjE0Njl9.WtEE28wchkNRX7CxYCbXY9kGs3Q9QLCwJyxpYqAI9_4  # Get the products list
- [GET] http://localhost:5000/products/12354656F234?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzAxMjE0Njl9.WtEE28wchkNRX7CxYCbXY9kGs3Q9QLCwJyxpYqAI9_4  # Get one product
- [GET] http://localhost:5000/products/currency/CAD?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzAxMjE0Njl9.WtEE28wchkNRX7CxYCbXY9kGs3Q9QLCwJyxpYqAI9_4  # Get the products list
- [GET] http://localhost:5000/products/CAD?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzAxMjE4NTV9.jXmf2QO4hrxPDFbtoOdSsRJ1rNeZBQF9PKRbLya1TAo  # Get the products list based on currency
- [POST] http://localhost:5000/products?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzAxMjE4NTV9.jXmf2QO4hrxPDFbtoOdSsRJ1rNeZBQF9PKRbLya1TAo  # Create a new product
        
        {
            "product_code": "12354656F234",
            "amount": 234.5,
            "currency_code": "USD"
        }
        
- [PUT] http://localhost:5000/products/12354656F234?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzAxMjE4NTV9.jXmf2QO4hrxPDFbtoOdSsRJ1rNeZBQF9PKRbLya1TAo  # Modify the whole product
        
        {
            "amount": 234.5,
            "currency_code": "USD"
        }
- [PATCH] http://localhost:5000/products/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzAxMjE4NTV9.jXmf2QO4hrxPDFbtoOdSsRJ1rNeZBQF9PKRbLya1TAo  # Modify some fields of the product
        
        {
            "amount": 234.5
        }
        
        or
        
        {
            "currency_code": "USD"
        }
- [DELETE] localhost:5000/products/product_code=12354656F234?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzAxMzM0ODl9.oHRrmapHqIgSuZKDFAKjW4dzHo17mJoAfsL7f8jwuKM  # Delete the product code