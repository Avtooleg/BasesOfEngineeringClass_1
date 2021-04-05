import RPi.GPIO as GPIO
import time
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy

GPIO.setmode(GPIO.BCM)

LED_nums = [24, 25, 8, 7, 12, 16, 20, 21] #nums of GPIO for real LEDs
DAC_nums = [10, 9, 11, 5, 6, 13, 19, 26] #nums of DAC inputs

GPIO.setup(DAC_nums, GPIO.OUT)


def num2dac(value):
    decNumber = int(value)
    bits = [0]*8
    for i in range(8):
        bits[i] = decNumber%2
        decNumber = decNumber//2
    GPIO.output(DAC_nums, bits)


try:
    while True:
        flag = True
        run = True

        while flag:
            try:
                name = input('Введите имя файла (-1 для выхода):')
                if name == '-1':
                    run = False
                    flag = False
                    break
                flag = False
            except FileNotFoundError:
                print('Имя файла некорректно, попробуйте ещё раз')
        if not run:
            break

        rate, data = scipy.io.wavfile.read(name+'.WAV')
        data = np.round(255*(data))
        for i in range(data):
            num2dac(i)
            time.sleep(1/rate)
finally:
    GPIO.output(DAC_nums, [0]*8)
    GPIO.cleanup()    