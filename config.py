from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'meow'
app.config['AWS_DOCUMENTDB_URI'] = 'ComingSoon'
app.config['MONGODB_URI'] = 'mongodb://127.0.0.1:27017'
