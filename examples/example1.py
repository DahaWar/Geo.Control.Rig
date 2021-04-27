from serial import Serial
from time import sleep
import TMCL
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QSlider, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import pyqtSlot


# serial-addressen er satt på TMCM module.
MODULE_ADDRESS = 1

#Kobler til serial_porten USB COM3
serial_port = Serial(port='COM3')

# Lager Bus instant ved bruk av open seriel port
bus = TMCL.connect(serial_port)

# Drar ut motor
motor = bus.get_motor(MODULE_ADDRESS)

## From this point you can start issuing TMCL commands
## to the motor as per the TMCL docs. This example will
## rotate the motor left at a speed of 1234 for 2 seconds

def utregning_fart():
    mmitimen = int(input("Hvilken hastighet vil du ha?"))
    hvorlenge = int(input("Hvor lenge skal den kjøre?"))
    RPH = (mmitimen / (5 * 3600))
    FSF = (RPH * 200)
    MSF = (FSF * 256)
    Velocity = ((MSF * 2048 * 32 * 8) / 16000000)
    print(Velocity)
    Fart = int(Velocity)
    motor.rotate_right(Fart)
    sleep(hvorlenge)

def ekstra_forskjyv():
    x = int(input("Hvor høy RPM: "))
    y = int(input("Hvor høy høyre RPM: "))
    motor.rotate_left(x)
    sleep(2)
    motor.rotate_right(y)
    sleep(2)

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

# Get the axis
# axis = bus.get_axis(MODULE_ADDRESS)


def window():
    app = QApplication(sys.argv)
    widget = QMainWindow()

    button_home = QPushButton(widget)
    button_home.setText("HOME")
    button_home.move(64, 32)
    button_home.clicked.connect(button_home_clicked)

    button_left = QPushButton(widget)
    button_left.setText("LEFT")
    button_left.move(64, 64)
    button_left.clicked.connect(button_left_clicked)

    button_right = QPushButton(widget)
    button_right.setText("RIGHT")
    button_right.move(64, 96)
    button_right.clicked.connect(button_right_clicked)

    button_help = QPushButton(widget)
    button_help.setText("HELP")
    button_help.move(900,20)
    button_help.clicked.connect(button_help_clicked)

    combo = QComboBox(widget)

    combo.addItem("10mm/h")
    combo.addItem("20mm/h")
    combo.addItem("40mm/h")
    combo.addItem("60mm/h")
    combo.addItem("80mm/h")
    combo.addItem("600mm/h")
    combo.move(64, 128)


    button_exit = QPushButton(widget)
    button_exit.setText("EXIT")
    button_exit.move(900, 500)
    button_exit.clicked.connect(button_exit_clicked)

    slider = QSlider(widget)
    slider.move(64, 300)

    selected_color = QColor(85, 170, 0)
    widget.setGeometry(250, 200, 1020, 600)
    widget.setWindowTitle("GEORIGG")
    widget.setStyleSheet("QWidget {background-color: %s}" % selected_color.name())
    widget.show()
    sys.exit(app.exec_())

def pop_window(self,text):

        msg = QMessageBox


        msg.setText("JADDAJADDA")
        msg.setWindowTitle("HELP")
        msg.setGeometry(50,50,500,300)
        msg.show()
        msg.exec_()

def button_home_clicked():
    print("GO TO HOME")
    motor.move_absolute(0)    #500000


def button_left_clicked():
    print("EXTRACTION")
    motor.move_absolute(-750000)


def button_right_clicked():
    print("CONTRACTION")
    motor.move_absolute(750000)

def button_help_clicked():
    pop_window()


def button_exit_clicked():
    print("Stop the application")
    motor.move_absolute(0)
    sleep(20)
    motor.stop()
    motor.stop_command()


if __name__ == '__main__':
   #utregning_fart()
   window()
    #motor.stop()
