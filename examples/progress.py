from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Help_Window(object):

    def setupUi(self, Georigg):
        Georigg.setObjectName("Georigg")
        Georigg.resize(600, 400)
        self.back_btn = QtWidgets.QPushButton(Georigg)
        self.back_btn.setGeometry(QtCore.QRect(250, 350, 113, 32))
        self.back_btn.setObjectName("back_btn")

        self.label = QtWidgets.QLabel(Georigg)
        self.label.setGeometry(QtCore.QRect(100, 30, 201, 71))
        self.label.setObjectName("label")
        self.retranslateUi(Georigg)
        QtCore.QMetaObject.connectSlotsByName(Georigg)

    def retranslateUi(self, Georigg):
        _translate = QtCore.QCoreApplication.translate
        Georigg.setWindowTitle(_translate("Georigg", "Help"))
        self.back_btn.setText(_translate("Georigg", "Back"))
        self.label.setText(_translate("Georigg", "HER SKAL DET STÅ INSTRUKSJONER OSV"))


class Ui_Georigg(object):

    def setupUi(self, Georigg):
        Georigg.setObjectName("Georigg")
        Georigg.resize(522, 355)
        self.label = QtWidgets.QLabel(Georigg)
        self.label.setGeometry(QtCore.QRect(140, 10, 191, 51))
        self.label.setStyleSheet("font: 36pt \".SF NS Text\";")
        self.label.setObjectName("label")

        self.help_btn = QtWidgets.QPushButton(Georigg)
        self.help_btn.setGeometry(QtCore.QRect(470, 10, 50, 32))
        self.help_btn.setObjectName("help_btn")

        self.button_exit = QtWidgets.QPushButton(Georigg)
        self.button_exit.setText("EXIT")
        self.button_exit.setGeometry(QtCore.QRect(470, 320, 50, 32))

        self.combo = QtWidgets.QComboBox(Georigg)
        self.combo.setGeometry(QtCore.QRect(140, 180, 113, 32))
        self.combo.addItem("Distance")
        self.combo.addItem("Time")
        self.combo.addItem("Distance/Time")
        self.combo.move(100, 200)

        self.retranslateUi(Georigg)
        QtCore.QMetaObject.connectSlotsByName(Georigg)

    def retranslateUi(self, Georigg):
        _translate = QtCore.QCoreApplication.translate
        Georigg.setWindowTitle(_translate("Georigg", "Georigg"))
        self.help_btn.setText(_translate("Georigg", "HELP"))


class Switchwindow(QtWidgets.QWidget, Ui_Georigg):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.help_btn.clicked.connect(self.pushbutton_handler)

    def pushbutton_handler(self):
        self.switch_window.emit()


class MainWindow(QtWidgets.QWidget, Help_Window):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.back_btn.clicked.connect(self.pushbutton_handler)


    def pushbutton_handler(self):
        self.switch_window.emit()


class Controller:

    def __init__(self):
        self.window = MainWindow()
        self.switch = Switchwindow()
        pass

    def show_switch(self):
        self.switch.switch_window.connect(self.show_main)
        self.window.close()
        self.switch.show()

    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_switch)

        self.window.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_switch()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
