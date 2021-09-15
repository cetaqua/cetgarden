import RPi.GPIO as GPIO
from .hx711 import HX711

class LoadCellSensor:

    def __setup_hx711(self, referenceUnits: float):
        self.__hx.set_reference_unit(referenceUnits)
        self.__hx.reset()
        self.__hx.tare()

    def __init__(self, data_collector, keyword: str, referenceUnits: float, dt_pin: int, sck_pin: int, num_measure: int, simulate=True):
        self.__data_collector = data_collector
        self.__keyword = keyword

        if not simulate:
            self.__hx = HX711(dt_pin, sck_pin)
            self.__setup_hx711(referenceUnits)

        self.__num_measure = num_measure
        self.__i = 0

    def getMeasure(self):
        val = self.__hx.get_weight(self.__num_measure)
        self.__hx.power_down()
        self.__hx.power_up()
        
        #send data to database

        return val

    def getSimulatedMeasure(self):
        self.__data_collector.add_data(self.__i, self.__keyword)
        self.__i += 1