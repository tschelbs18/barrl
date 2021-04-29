import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
# loop through 3 times, on for 5 seconds/off for 1 second
for i in range(3):
    GPIO.output(7,True)
    time.sleep(5)
    GPIO.output(7,False)
    time.sleep(1)
GPIO.cleanup()
