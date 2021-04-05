import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_nums = [24, 25, 8, 7, 12, 16, 20, 21] #nums of GPIO for real LEDs
DAC_nums = [10, 9, 11, 5, 6, 13, 19, 26] #nums of DAC inputs

GPIO.setup(DAC_nums, GPIO.OUT)


def to_LED(states):
    global LED_nums
    nums = []
    state = []
    for i in states:
        nums.append(LED_nums[i[0]])
        state.append(i[1])
    GPIO.setup(nums, GPIO.OUT)
    for i in states:
        GPIO.output(LED_nums[i[0]], i[1])


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

def run():
    try:
        while True:
            flag = True
            run = True

            while flag:
                try:
                    request = int(input('Введите число (-1 для выхода):'))
                    if 0<=request<=255:
                        flag = False
                    elif request == -1:
                        run = False
                        flag = False
                    else:
                        print('Введите, пожалуйста, число от 0 до 255')
                except ValueError:
                    print('Число неккоректно, попробуйте ещё раз')
                
            if not run:
                break

            num2dac(request)
    finally:
        GPIO.output(DAC_nums, [0]*8)
        GPIO.cleanup()
run()