from pymongo import MongoClient

client = MongoClient('mongodb://root:123456@localhost:27017/')
print(client.list_database_names())
db = client['test']


collection = db['art_station']

stu1={'id':'001','name':'zhangsan','age':10}
result = collection.insert_one(stu1)
print(result)