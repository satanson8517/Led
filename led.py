import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

while True:
    GPIO.output(11, True)
    time.sleep(1)
    GPIO.output(12, True)
    time.sleep(1)
    GPIO.output(13, True)
    time.sleep(1)
    GPIO.output(11, False)
    time.sleep(1)
    GPIO.output(12, False)
    time.sleep(1)
    GPIO.output(13, False)
    time.sleep(1)

