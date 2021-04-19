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
        for i in range(255):
            time.sleep(0.0005)
            before = GPIO.input(4)
            Lib.num2dac(i)
            time.sleep(0.0005)
            after = GPIO.input(4)
            if after != before or (after == 0 and before == 0):
                SIG_new = i
                break
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
