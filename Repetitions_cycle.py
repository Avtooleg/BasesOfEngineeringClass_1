import RPi.GPIO as GPIO
import time
#from Number_to_Volts import num2dac
import math

GPIO.setmode(GPIO.BCM)

LED_nums = [24, 25, 8, 7, 12, 16, 20, 21] #nums of GPIO for real LEDs
DAC_nums = [10, 9, 11, 5, 6, 13, 19, 26] #nums of DAC inputs

GPIO.setup(DAC_nums, GPIO.OUT)


def num2dac(value):
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


def repeatition(repetitionsNumber, sinus=False):
    for i in range(repetitionsNumber):
        for j in range(256):
            num2dac(j)
            time.sleep(0.01)
        for j in range(256, -1, -1):
            num2dac(j)
            time.sleep(0.01)
    GPIO.output(DAC_nums, [0]*8)


try:
    while True:
        flag = True
        run = True

        while flag:
            try:
                request = int(input('Введите число повторений (-1 для выхода):'))
                if request>0:
                    flag = False
                elif request == -1:
                    run = False
                    flag = False
                else:
                    print('Введите, пожалуйста, число больше нуля')
            except TypeError:
                print('Число неккоректно(нецело, криво, косо), попробуйте ещё раз')
        if not run:
            break

        repeatition(request)
finally:
    GPIO.output(DAC_nums, [0]*8)
    GPIO.cleanup()