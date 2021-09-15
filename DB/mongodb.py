"""
Created on Fri Sept 4 10:01 2020

@author: Alejandro Palomino
"""

from DB.abstract_database import Abstract_Database
from DB.mongoDBException import MongoDBException
import pymongo
from typing import Dict, List

class Database(Abstract_Database):
    
    def __init__(self, db_name):
        Abstract_Database.__init__(self, db_name)

    def _connect(self) -> pymongo.mongo_client.MongoClient:
        ''' 
        Return a database client -> MongoClient
        '''
        client = pymongo.MongoClient("mongodb://{}:{}@{}:{}".format(self.get_username(), self.get_password(), self.get_ip(), self.get_port()))
        return client

    def _close_connection(self, client):
        '''
        Close connection from a client

        client -> MongoClient: client that you want to close the connection with the database
        '''
        client.close()

    def execute_query(self, dict_query: dict, str_collection: str, dict_fields=None) -> pymongo.cursor.Cursor:
        ''' 
        Ejecute query and get the result 

        :param dict dict_query
        :param str_collection: collection where get data 
        :param dict dict_fields: specify the fields to get from data, default value get all fields

        '''
        #Connect to database
        client = self._connect()
        db = client[self.get_db_name()]

        #Get data from database
        collection = db[str_collection]
        documents = collection.find(dict_query, dict_fields)

        #Close connection
        self._close_connection(client)

        return documents


    def send_data_query(self, str_collection, data: Dict):
        # Connect to database
        client = self._connect()
        db = client[self.get_db_name()]

        try:
            collection = db[str_collection]
            collection.insert(data)

        except:
            raise MongoDBException(msg="Error sending data to bd")
            
        finally:
            #Close connection
            self._close_connection(client)


    def send_multiples_data_query(self, datas: List["data"]):
        '''
        Not working yet
        '''
        pass
        # #Connect to database
        # client = self._connect()
        # db = client[self.get_db_name()]

        # for data in datas:
        #     try:
        #         # destination = 'USERS'
        #         # collection = client[MONGODB_DATABASE][destination]
        #         # collection.insert(data)
        #         pass
                
        #     except Exception as error:
        #         print("Error savind data: " + str(error))
        #         continue

        # #Close connection
        # self._close_connection(client)
