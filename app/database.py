import pymongo
from config import *


class DB(object):
    URI = app.config['MONGODB_URI']

    @staticmethod
    def init():
        client = pymongo.MongoClient(DB.URI)
        DB.DATABASE = client['products']

    @staticmethod
    def insert_one(collection, data):
        return DB.DATABASE[collection].insert_one(data)

    @staticmethod
    def find_one(collection, query):
        return DB.DATABASE[collection].find_one(query)

    @staticmethod
    def replace_one(collection, query):
        return DB.DATABASE[collection].replace_one(query)

    @staticmethod
    def find(collection, query):
        return DB.DATABASE[collection].find(query)

    @staticmethod
    def delete_one(collection, query):
        return DB.DATABASE[collection].delete_one(query)
