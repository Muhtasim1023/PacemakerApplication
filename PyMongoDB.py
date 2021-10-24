import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://Cameron:Password@cluster0.v2lpn.mongodb.net/test?retryWrites=true&w=majority")

db = cluster["test"]
collection = db["test"]

# Database -> Collection -> Post -> Fields

# {"_id": 0, "Name": "Tim", "Score": 5} This is a post

post = {"_id": 0, "Name": "Tim", "Score": 5}

collection.insert_one(post)