import time
from adfruit_servokit import ServoKit

nbPCAServo = 16
pca = ServoKit(channels =16)
for i in range(nbPCAServo):
    pca.servo[i].set_pulse_width_range(500,2500)

#To set angle
pca.servo[0].angle = 30 
#To disable Channel
pca.servo[0].angle = None


