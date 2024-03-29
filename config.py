from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'meow'
app.config['AWS_DOCUMENTDB_URI'] = 'ComingSoon'
app.config['MONGODB_URI'] = 'mongodb://127.0.0.1:27017'
app.config['DISABLE_TOKEN'] = False
app.config['TOKEN_EXPIRED_SECONDS'] = 10000
app.config['DEBUG'] = True
app.config['HOST'] = 'localhost'
app.config['PORT'] = 5000
