import pandas as pd
import numpy as np
import pymongo
import json
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from urllib.parse import quote_plus

# MongoDB credentials (ensure you encode special characters in password)
username = "216963shrutiahuja"
password = quote_plus("Admin@123")
MONGODB_URL = f"mongodb+srv://{username}:{password}@cluster0.4mtunmb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def cv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            mongo_client = pymongo.MongoClient(MONGODB_URL)
            db = mongo_client[database]
            coll = db[collection]
            coll.insert_many(records)
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == '__main__':
    FILE_PATH = 'network_data/Phishing_Legitimate_full.csv'
    DATABASE = 'SHRUTU'
    COLLECTION = 'NetworkData'

    networkobj = NetworkDataExtract()

    # Correct: assign the returned value to 'records'
    records = networkobj.cv_to_json_convertor(file_path=FILE_PATH)
    print(records)

    # Insert into MongoDB and print count
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)
    print(f"{no_of_records} records inserted successfully.")
