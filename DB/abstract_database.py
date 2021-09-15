"""
Created on Fri Sept 4 09:39 2020

@author: Alejandro Palomino
"""
from abc import ABCMeta, abstractmethod
from typing import List

class Abstract_Database(metaclass=ABCMeta):
    def __init__(self, db_name: str, ip="", port="", username="", password=""):
        self._ip = ip
        self._port = port
        self._username = username
        self._password = password
        self._db_name = db_name


    def get_ip(self) -> str:
        return self._ip

    def set_ip(self, ip):  
        self._ip = ip

    def get_port(self) -> str:
        return self._port

    def set_port(self, port):
        self._port = port

    def get_username(self) -> str:
        return self._username

    def set_username(self, username):
        self._username = username

    def get_password(self) -> str:
        return self._password

    def set_password(self, password):
        self._password = password

    def get_db_name(self) -> str:
        return self._db_name

    def set_db_name(self, db_name):
        self._db_name = db_name

    @abstractmethod
    def _connect(self) -> 'Abstract_Database':
        pass

    @abstractmethod
    def execute_query(self):
        pass

    @abstractmethod
    def send_data_query(self, data):
        pass

    @abstractmethod
    def send_multiples_data_query(self, datas: List["data"]):
        pass

    @abstractmethod
    def _close_connection(self):
        pass
