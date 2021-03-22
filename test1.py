import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_nums = [24, 25, 8, 7, 12, 16, 20, 21] #nums of GPIO for real LEDs


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


def lightUp(ledNumber, period):
    to_LED([[ledNumber, 1]])
    time.sleep(period)
    to_LED([[ledNumber, 0]])


def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range(blinkCount):
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)


def runningLight(count, period):
    for i in range(count):
        for j in range(8):
            lightUp(j, period)


def runningDark(count, period):
    for i in range(count):
        for j in range(8):
            leds = []
            for k in range(8):
                if k != j:
                    leds.append([k,1])
            to_LED(leds)
            time.sleep(period)
            for k in leds:
                k[1] = 0
            to_LED(leds)


def decToBinList(decNumber):
    bits = []
    if decNumber<0 or decNumber>255:
        print("INVALID NUMBER, USE FROM THE RANGE 0...255")
        return
    while decNumber > 0:
        bits.append(decNumber%2)
        decNumber = decNumber//2
    while len(bits)<8:
        bits.append(0)
    bits = list(reversed(bits))
    return bits


def lightNumber(number, period=3):
    if number<0 or number>255:
        print("INVALID NUMBER, USE FROM THE RANGE 0...255")
        return
    bits = list(reversed(decToBinList(number)))
    leds = []
    for i in range(8):
        leds.append([i, bits[i]])
    to_LED(leds)
    time.sleep(period)
    for i in leds:
        i[1] = 0
    to_LED(leds)


def runningPattern(pattern, direction, time_=0, period=0.2):
    if pattern<0 or pattern>255:
        print("INVALID NUMBER, USE FROM THE RANGE 0...255")
        return
    bits = list(reversed(decToBinList(pattern)))
    if direction == "r":
        direction = 1
    elif direction == "l":
        direction = -1
    else:
        print("INVALID DIRECTION, USE r or l")
        return
    leds = []
    for i in range(8):
        leds.append([i, 0])
    if time_ == 0:
        while True:
            for i in range(len(bits)):
                leds[i][1] = bits[i]
            to_LED(leds)
            bits_new = []
            for i in range(len(bits)):
                bits_new.append(bits[(i+direction)%8])
            bits = bits_new
            time.sleep(period)
    else:
        time_0 = time.real()
        while time.real() - time_0 < time_:
            for i in range(len(bits)):
                leds[i][1] = bits[i]
            to_LED(leds)
            bits_new = []
            for i in range(len(bits)):
                bits_new.append(bits[(i+direction)%8])
            bits = bits_new
            time.sleep(period)



def PWM_Blinking(ledNumber, period, time_):
    GPIO.setup(LED_nums[ledNumber], GPIO.OUT)
    p = GPIO.PWM(LED_nums[ledNumber], 50)
    p.start(0)
    time_0 = time.clock()
    while time.clock()- time_0 < float(time_)/100:
        for i in range(0, 101, 5):
            p.ChangeDutyCycle(i)
            time.sleep(float(period)/200)
        for i in range(100, -1, -5):
            p.ChangeDutyCycle(i)
            time.sleep(float(period)/200)
    p.stop()


PWM_Blinking(1, 1, 10)





GPIO.cleanup()