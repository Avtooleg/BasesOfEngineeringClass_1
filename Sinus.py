import RPi.GPIO as GPIO
import time
import math
import numpy as np
import matplotlib.pyplot as plt

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


def sinus(freq, time_, sampleRate):
    init_range = np.linspace(0, time_, round(time_*sampleRate))
    w = freq*2*math.pi
    amp = np.round(127.5*(np.sin(w*init_range)+1))
    plt.plot(init_range, amp)
    plt.show()
    t0 = time.perf_counter()
    print(len(amp)/sampleRate)
    for i in amp:
        num2dac(i)
        time.sleep(1/sampleRate)
    print(time.perf_counter()-t0)
    GPIO.output(DAC_nums, [0]*8)

try:
    while True:
        flag = True
        run = True

        while flag:
            try:
                frequency = float(input('Введите частоту (Гц) синусоиды (-1 для выхода):'))
                if frequency == -1:
                    run = False
                    flag = False
                    break
                samplingFrequency = float(input('Введите частоту дискретизации (Гц):'))
                time_ = float(input('Введите дилтельность проигрывания:'))
                if frequency>0 and samplingFrequency>0 and time_>0:
                    flag = False
                else:
                    print('Введите, пожалуйста, число больше нуля')
            except TypeError:
                print('Число неккоректно(нецело, криво, косо), попробуйте ещё раз')
        if not run:
            break

        sinus(frequency, time_, samplingFrequency)
finally:
    GPIO.output(DAC_nums, [0]*8)
    GPIO.cleanup()    