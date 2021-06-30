import time
import subprocess

import RPi.GPIO as GPIO

from util import timer
from util import config
from net import kunapi

MOTION_SENSOR_PIN = 14

def setup():
    GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)

def update(motion):
    if GPIO.input(MOTION_SENSOR_PIN):
        if not motion:
            motion = True
            subprocess.run('vcgencmd display_power 1', shell=True)
            kunapi.status(3)
    else:
        if motion:
            motion = False
            kunapi.status(4)
            # dont know if i want to do this just yet
            #subprocess.run('vcgencmd display_power 0', shell=True)

    time.sleep(3)
    return
    