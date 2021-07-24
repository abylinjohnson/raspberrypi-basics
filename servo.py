import RPi.GPIO as GPIO
import time
servo = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)
pwm=GPIO.PWM(servo,50)
pwm.start(0)

def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo, False)
    pwm.ChangeDutyCycle(0)

setAngle(90)

pwm.stop()
GPIO.cleanup()


