#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Libraries
import time  # https://docs.python.org/fr/3/library/time.html
# https://circuitpython.readthedocs.io/projects/servokit/en/latest/
from adafruit_servokit import ServoKit
import keyboard
# Constants
nbPCAServo = 6
# Parameters
MIN_IMP = [500, 500, 500, 500, 500, 500, 500,
           500, 500, 500, 500, 500, 500, 500, 500, 500]
MAX_IMP = [2500, 2500, 2500, 2500, 2500, 2500, 2500,
           2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
MIN_ANG = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MAX_ANG = [180, 180, 180, 180, 180, 180, 180,
           180, 180, 180, 180, 180, 180, 180, 180, 180]
# Objects
pca = ServoKit(channels=16)
# function init


def init():
    for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i], MAX_IMP[i])
# function main


def main():
    pick_pos = int(input("Enter the Pic ang:"))
    drop_pos = int(input("Enter the drop ang:"))
    pick(pick_pos)
    drop()
# function pcaScenario


def pcaScenario():
    """Scenario to test servo"""
    for i in range(nbPCAServo):
        for j in range(MIN_ANG[i], MAX_ANG[i], 1):
            print("Send angle {} to Servo {}".format(j, i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        for j in range(MAX_ANG[i], MIN_ANG[i], -1):
            print("Send angle {} to Servo {}".format(j, i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        pca.servo[i].angle = None  # disable channel
        time.sleep(0.5)


def keyboardCtrl():
    for i in range(6):
        pca.servo[i].angle = 0
        time.sleep(0.5)
    a0 = 0
    while True:
        if keyboard.is_pressed('a'):
            if a0 < 180:
                a0 = a0 + 1
                pca.servo[0].angle = a0
        if keyboard.is_pressed('d'):
            if a0 > 0:
                a0 = a0 - 1
                pca.servo[0].angle = a0


def pick(a):
    pca.servo[0].angle = a
    pca.servo[1].angle = 75
    pca.servo[5].angle = 75
    pca.servo[1].angle = 75
    pca.servo[1].angle = 75
    pca.servo[1].angle = 75
    pca.servo[1].angle = 75


def drop(d):
    pca.servo[0].angle = d
    pca.servo[1].angle = 75
    pca.servo[5].angle = 75
    pca.servo[1].angle = 75
    pca.servo[1].angle = 75
    pca.servo[1].angle = 75
    pca.servo[1].angle = 75
