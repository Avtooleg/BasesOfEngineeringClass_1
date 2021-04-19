import Lib
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_nums = [24, 25, 8, 7, 12, 16, 20, 21] #nums of GPIO for real LEDs
DAC_nums = [10, 9, 11, 5, 6, 13, 19, 26] #nums of DAC inputs

GPIO.setup(17, GPIO.OUT)
GPIO.output(17, 1)

try:
    Lib.startup()
    while True:
        num = int(input("Enter a guess number(-1 to exit)> "))
        if num == -1:
            break
        print(num, "=", round(3.3*num/255, 2), "V")
        Lib.num2dac(num)
finally:
    GPIO.output(DAC_nums + [17], [0]*9)
    GPIO.cleanup()