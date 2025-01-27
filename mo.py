from pymongo import MongoClient
import requests
client = MongoClient("mongodb+srv://user:user@cluster0.u3fdtma.mongodb.net/linkey")
db = client.linkey
comment_db = db.comment
db = db.all
# db.create_index([("title", "text")])
data = db.find({}, {"_id": 0})
print(data)


db.update_one(
    {"unique_id": 27},
    {"$set": {"comments": 1}}
)