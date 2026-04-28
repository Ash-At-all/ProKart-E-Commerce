from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)

db = client["prokart"]

cart_collection = db["cart"]
user_collection = db["users"]
products_collection = db["products"]
orders_collection = db["orders"]


