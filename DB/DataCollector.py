from threading import Semaphore
from typing import List
from datetime import datetime
from typing import Dict
from DB.mongodb import Database
from datetime import datetime

class DataCollector:

    def __init__(self, DB_name: str, collection_name: str ,keywords: List[str], keys_to_check_to_send_data: List[str]):
        #Check if keys_to_check_to_send_data is a subset of keywords
        if not self.__isSubSet(keys_to_check_to_send_data, keywords):
            raise Exception

        self.__data = dict()
        self.__keys_to_check_to_send_data = keys_to_check_to_send_data
        
        for key in keywords:
            self.__data[key] = list()

        self.__db = Database(DB_name)
        self.__collection = collection_name
        self.__semaphore = Semaphore()

    def add_data(self, data, keyword: str):
        print("add : " + keyword)
        self.__semaphore.acquire()
        if not keyword in self.__data:
            self.__semaphore.release()
            raise Exception

        self.__data[keyword].append(data)

        # If pack of data is complete, send to database
        if self.__ready_for_send_to_db():
            #Create dict to send to mongo db
            data = dict()
            data["tiempo"] = datetime.now()
            for key in self.__keys_to_check_to_send_data:
                data[key] = self.__data[key].pop(0)
            
            #Send to mongo
            self.__db.send_data_query(self.__collection, data)
        self.__semaphore.release()

    def __ready_for_send_to_db(self):
        res = True
        for key in self.__keys_to_check_to_send_data:
            if len(self.__data[key]) == 0:
                res = False
                break
        return res

    def __isSubSet(self, set1: List[str], set2: List[str]) -> bool:
        res = True
        for item in set1:
            if item not in set2:
                res = False
                break
        return res

    def get_data(self) -> Dict[str, any]:
        self.__semaphore.acquire()
        data_copy = self.__data.copy()
        self.__semaphore.release()
        return data_copy