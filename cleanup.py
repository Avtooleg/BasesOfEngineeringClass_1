import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LED_nums = [26, 19, 13, 6, 5, 11, 9, 10, 21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(LED_nums, GPIO.OUT)
GPIO.output(LED_nums, 0)

GPIO.cleanup()