import RPi.GPIO as GPIO
import time
import math
import numpy as np

LED_nums = [24, 25, 8, 7, 12, 16, 20, 21] #nums of GPIO for real LEDs
DAC_nums = [10, 9, 11, 5, 6, 13, 19, 26] #nums of DAC inputs

def startup(): #Startup of module and set of GPIO
    GPIO.setup(DAC_nums, GPIO.OUT)
    GPIO.setup(LED_nums, GPIO.OUT)

def shutdown(): #shutdown of module and reset of GPIO
    GPIO.output(DAC_nums, [0]*8)
    GPIO.output(LED_nums, [0]*8)
    GPIO.cleanup()
def num2dac(value): #dec num to bin num and into DAC
    bits = []
    if value<0 or value>255:
        print("INVALID NUMBER, USE FROM THE RANGE 0...255")
        return
    decNumber = value
    while decNumber > 0:
        bits.append(decNumber%2)
        decNumber = decNumber//2
    while len(bits)<8:
        bits.append(0)
    nums = [DAC_nums[i] for i in range(len(bits))]
    GPIO.output(nums, bits)