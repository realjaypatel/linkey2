from pymongo import MongoClient
import requests
client = MongoClient("mongodb+srv://user:user@cluster0.u3fdtma.mongodb.net/linkey")
db = client.linkey
db = db.all


db.create_index([("title", "text")])
data = list(db.find({"title": {"$regex": 'bera', "$options": "i"}}))
print(data)