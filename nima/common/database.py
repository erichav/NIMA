import pymongo
import os
from nima.models.baseError import DocumentDoesNotExist


class Database():
    URI = os.environ.get('MONGODB_URI')
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client.get_database()

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        res = Database.DATABASE[collection].find(query)
        if res:
            return res
        raise DocumentDoesNotExist(f"El documento de la coleccion {collection} no fue encontado")



    @staticmethod
    def find_one(collection, query):
        res = Database.DATABASE[collection].find_one(query)
        if res is None:
            raise DocumentDoesNotExist(f"El documento de la coleccion {collection} no fue encontado")
        return res

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        return Database.DATABASE[collection].remove(query)

    @staticmethod
    def aggregate(collection, queries):
        return Database.DATABASE[collection].aggregate(queries)
