# This ensures we can gain intelisense functionality in VSCode by importing from our header file
# at ../spike/spike.py
import os
if hasattr(os,'name'):
    from spike.spike import *
else:
    # put all SPIKE imports in this block
    from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair

# any non-spike imports that LEGO supports can go here
from math import *

# Sample interaction with the hub display
hub = PrimeHub()
hub.light_matrix.show_image('HAPPY')

# Sample Motor Init function
def init_motors(left,right):
    mp = MotorPair(left,right)
    mp.set_default_speed(50)
    # set wheel diameter
    mp.set_motor_rotation(17.5, "cm")
    return mp

# Sample init motor pair with A and E and run it
mp = init_motors('A','E')
mp.move(10)
