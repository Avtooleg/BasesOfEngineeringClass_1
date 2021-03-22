import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

p = GPIO.PWM(21, 50)
p.start(0)

while True:
    for i in range(0, 101, 2):
        p.ChangeDutyCycle(i)
        time.sleep(0.1)
    for i in range(100, -1, -2):
        p.ChangeDutyCycle(i)
        time.sleep(0.1)