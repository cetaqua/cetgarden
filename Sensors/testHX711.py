from LoadCell import LoadCellSensor
import time

lc = LoadCellSensor(None, None, -300/1000, 5, 6, 5)

while True:
    print(lc.getMeasure())
    time.sleep(2)