from pymongo import MongoClient
import requests
client = MongoClient("mongodb+srv://user:user@cluster0.u3fdtma.mongodb.net/linkey")
db = client.linkey
comment_db = db.comment

# db.create_index([("title", "text")])
data = list(comment_db.find({'post_id': '20'}))
print(data)