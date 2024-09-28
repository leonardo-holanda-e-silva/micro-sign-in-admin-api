import logging
import uuid

from pymongo import MongoClient
from pymongo.errors import PyMongoError

logging.basicConfig(level=logging.INFO)

class MongoService:
    def __init__(self, uri: str, database: str):
        try:
            self.client = MongoClient(uri)
            self.db = self.client[database]
            self.collection = self.db['registry']
        except PyMongoError as e:
            logging.error(f"Error connecting to MongoDB: {e}")
            raise e

    def insert_schema(self, schema: dict):
        try:
            if 'key' not in schema:
                schema['key'] = str(uuid.uuid4())

            result = self.collection.insert_one(schema)
            return result.inserted_id
        except PyMongoError as e:
            logging.error(f"Error inserting schema: {e}")
            return None

    def get_schema_by_key(self, key: str):
        try:
            schema = self.collection.find_one({"key": key})
            if schema:
                schema['_id'] = str(schema['_id'])
            return schema
        except PyMongoError as e:
            logging.error(f"Error fetching schema: {e}")
            return None
