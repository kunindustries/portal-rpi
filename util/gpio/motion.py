import time
import subprocess

import RPi.GPIO as GPIO

from util import timer
from util import config
from net import kunapi

MOTION_SENSOR_PIN = 14

motion = False

def setup():
    GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)

def display_power_on():
    return subprocess.run('vcgencmd display_power 1', shell=True)

def display_power_off():
    return subprocess.run('vcgencmd display_power 0', shell=True)

def is_display_powered():
    # ask if the display is already powered on
    result = subprocess.run('vcgencmd display_power -1', shell=True, capture_output=True)
    output = str(result.stdout)
    if str(output) != "b'display_power=1\\n'":
        return True
    else:
        return False

def get_idle_time():
    result = subprocess.run('export DISPLAY=:0 && sudo -u pi xprintidle', shell=True, capture_output=True)
    output = str(result.stdout)
    output = output[2:len(output) - 3]
    idletime = int(output)
    return idletime

def update():
    global motion

    if GPIO.input(MOTION_SENSOR_PIN):
        if not motion:
            motion = True
            print("motion detected")
            kunapi.status(3)

            if is_display_powered():
                display_power_on()
    else:
        if motion:
            motion = False
            print("motion no longer detected")
            kunapi.status(4)
        elif not motion and not is_display_powered():
            if get_idle_time() > (config.screen_idle_time * 1000):
                display_power_off()
    return