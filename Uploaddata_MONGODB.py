from pymongo import MongoClient
import os
from dotenv import load_dotenv
from database import products

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client["prokart"]
products_collection = db["products"]

products_collection.delete_many({})
products_collection.insert_many(products)
print(f"✅ {len(products)} products MongoDB mein upload ho gaye")