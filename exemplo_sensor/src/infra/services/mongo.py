import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

MONGODB_URL = os.environ.get("MONGODB_URL", None)

client = MongoClient(MONGODB_URL, server_api=ServerApi('1'))
