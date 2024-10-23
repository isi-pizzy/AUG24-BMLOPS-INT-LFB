from pymongo import MongoClient

client = MongoClient("mongodb://admin:R0vTrwRkhguP0tK4@mongodb:27017/lfb?retryWrites=true&w=majority")
db = client.get_database('lfb')
print(db.list_collection_names())
