import numpy as np 
import pandas as pd 
import pymongo

import os 
import sys 
import json 

from src.logging.logger import logging
from src.exception.exception import CustomException

import certifi 

from dotenv import load_dotenv
load_dotenv()

mongoDb_url = os.getenv("MONGO_DB_URL")
print(mongoDb_url)

ca = certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
    
    def cv_to_json_converter(self,file_path):
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True,inplace=True)
            records = list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            raise CustomException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        self.datbase = database 
        self.collection = collection 
        self.records = records

        self.mongo_client = pymongo.MongoClient(mongoDb_url)
        self.datbase = self.mongo_client[self.datbase]
        self.collection = self.datbase[self.collection]
        self.collection.insert_many(self.records)

        return(len(self.records))

if __name__ == '__main__':
    file_path = 'Network_data\phisingData.csv'
    database = 'vittal2001'
    collection = 'Network_data'
    networkDataExtract = NetworkDataExtract()
    records = networkDataExtract.cv_to_json_converter(file_path)
    print(records)
    no_of_records = networkDataExtract.insert_data_mongodb(records,database,collection)
    print(no_of_records)

