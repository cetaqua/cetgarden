#from Sensors.LoadCell import LoadCellSensor
import random

dt_pin = 5
sck_pin = 6
num_measures = 5
referenceUnits = 1 #1 para calibrar
known_weight = 1000 #Peso en gramos 

num_measures_to_calculate_mean = 100

#lc = LoadCellSensor(None, "Celda de carga", referenceUnits, dt_pin, sck_pin, num_measures)
measures = list()

i = 0
rd = random.Random()
while i < num_measures_to_calculate_mean:
    # measures.append(lc.getMeasure())
    measures.append(rd.random()*3000)
    i += 1

mean = sum(measures) / num_measures_to_calculate_mean
result = mean / known_weight
print("Unidades de refencia para el sensor calibrado: ", result)

