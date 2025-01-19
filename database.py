from pymongo import MongoClient
import requests
client = MongoClient("mongodb+srv://user:user@cluster0.u3fdtma.mongodb.net/linkey")
db = client.linkey
db = db.all