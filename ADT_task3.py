import Lib
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.output(17, 1)

GPIO.setup(4, GPIO.IN)


try:
    SIG_prev = 0
    Lib.startup()
    while True:
        GPIO.output(Lib.DAC_nums, [0]*8)
        left = 0
        right = 255
        while right-left>1:
            curr_guess = left + (right-left)//2
            Lib.num2dac(curr_guess)
            time.sleep(0.01)
            if GPIO.input(4):
                left = curr_guess
            else:
                right = curr_guess
        SIG_new = curr_guess
        if abs(SIG_new - SIG_prev) > 2:
            SIG_prev = SIG_new
            print("Digital value: ", SIG_new, "Analog value: ", round(3.3*SIG_new/255, 2))
except KeyboardInterrupt:
    GPIO.output(17, 0)
    Lib.shutdown()
    GPIO.cleanup()
finally:
    GPIO.output(17, 0)
    Lib.shutdown()
    GPIO.cleanup()