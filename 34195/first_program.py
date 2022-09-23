from spike.spike import *

mp = MotorPair('E','A')
mp.set_default_speed(50)
mp.set_motor_rotation(5.6,'cm')

mp.move(50,'cm')
