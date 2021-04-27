from serial import Serial
from time import sleep
import TMCL
import sys

## serial-addressen er satt på TMCM module.
MODULE_ADDRESS = 1

## Kobler til serial_porten USB COM3
serial_port = Serial(port="COM3")

## Lager Bus instant ved bruk av open seriel port
bus = TMCL.connect(serial_port)

## Drar ut motor
motor = bus.get_motor(MODULE_ADDRESS)

def  toekstra_forskjyv():
    #x = int(input("Hvor høy RPM: "))
    #y = int(input("Hvor høy høyre RPM: "))
    motor.rotate_left(1234)
    sleep(2)
    motor.rotate_right(1234)
    sleep(2)
    motor.stop()
    motor.stop_command()

def Sett_posisjon():
    z = int(input("Sett in posisjon fra -5 til 10:" ))
    calc_z = z*100000
    motor.move_absolute(calc_z)
    sleep(30)

def Home_position():
    answer = input("back to home position?: ")
    if answer == "ja":
        motor.move_absolute(0)
    else:
        return motor.stop()

def movecoord():
    answer = input("back to home position?: ")
    motor.move_coordinate(answer)
