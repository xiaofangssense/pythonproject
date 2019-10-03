# pythontestproject
##Prequisted
- Make sure the latest official python and pip are installed, could be python 3.7, and pip3
##Getting Started
- Python -m pip install -r requirements.txt
- python main.py
##Endpoints
- localhost:5000  # Hello world
- [GET] http://localhost:5000/login  # Get the token, could be: `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzAxMjA3NDZ9._uRInw6C2wdTW5AVwqGYSLw-lA0gj_naUcAw0s5z8k0`
- [GET] http://localhost:5000/products?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzAxMjE0Njl9.WtEE28wchkNRX7CxYCbXY9kGs3Q9QLCwJyxpYqAI9_4  # Get the products list
- [GET] http://localhost:5000/products/CAD?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzAxMjE0Njl9.WtEE28wchkNRX7CxYCbXY9kGs3Q9QLCwJyxpYqAI9_4  # Get the products list
- [GET] http://localhost:5000/products/CAD?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzAxMjE4NTV9.jXmf2QO4hrxPDFbtoOdSsRJ1rNeZBQF9PKRbLya1TAo  # Get the products list based on currency
- [POST] http://localhost:5000/products/CAD?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzAxMjE4NTV9.jXmf2QO4hrxPDFbtoOdSsRJ1rNeZBQF9PKRbLya1TAo  # Get the products list based on currency
        
        {
            "product_code": "12354656F234",
            "amount": 234.5,
            "currency_code": "USD"
        }
- [PUT] http://localhost:5000/products/CAD?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NzAxMjE4NTV9.jXmf2QO4hrxPDFbtoOdSsRJ1rNeZBQF9PKRbLya1TAo  # Get the products list based on currency
        
        {
            "product_code": "12354656F234",
            "amount": 234.5,
            "currency_code": "USD"
        }
- [DELETE]