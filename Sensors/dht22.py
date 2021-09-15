import time
import board
import adafruit_dht

#Sensor for temperature and humidity
class DHT22:

    def __init__(self, data_collector, keyword_temp: str, keyword_hum: str):
        self.__data_collector = data_collector
        self.__count = 0
        self.__keyword_temp = keyword_temp
        self.__keyword_hum = keyword_hum
        self.__device = adafruit_dht.DHT22(board.D4)

    def getMeasure(self):
        #Add temperature and humidity measured from the sensor
        self.__data_collector.add_data(self.__device.humidity, self.__keyword_hum)
        self.__data_collector.add_data(self.__device.temperature, self.__keyword_temp)
            