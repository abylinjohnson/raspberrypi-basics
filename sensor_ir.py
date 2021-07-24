import RPi.GPIO as GPIO
import time

s = 40
led = 10
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(s, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 0)

while True:
     
    if GPIO.input(s)==0:
        print("connected")
        GPIO.output(led, 1)
        time.sleep(0.2)
    else:
        print("Not Connected")
        GPIO.output(led, 0)
        time.sleep(0.2)

