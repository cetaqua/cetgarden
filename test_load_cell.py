from hx711 import HX711
import RPi.GPIO as GPIO
from typing import List


def mean(data: List[int]):
    N = len(data)
    acc = 0
    for value in data:
        acc += value

    return acc / N

try:
    hx711 = HX711(
        dout_pin=21,
        pd_sck_pin=20,
        channel='A',
        gain=64
    )

    hx711.reset()   # Before we start, reset the HX711 (not obligate)
    measures = hx711.get_raw_data(6)
finally:
    GPIO.cleanup()  # always do a GPIO cleanup in your scripts!

print("Peso: ", mean(measures))
print("\n", measures)