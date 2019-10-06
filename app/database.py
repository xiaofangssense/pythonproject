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
        return list(DB.DATABASE[collection].find_one(query))

    @staticmethod
    def find_one_and_replace(collection, query, replace):
        return DB.DATABASE[collection].find_one_and_replace(query, replace)

    @staticmethod
    def find_one_and_update(collection, query, update):
        return DB.DATABASE[collection].find_one_and_update(query, {"$set": update}, upsert=True)

    @staticmethod
    def find(collection, query):
        # Find all products
        products = DB.DATABASE[collection].find(query)
        return list(products)

    @staticmethod
    def delete(collection, query):
        return DB.DATABASE[collection].delete_many(query)
