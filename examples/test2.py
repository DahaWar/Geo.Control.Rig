# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

#from TMCL import Scripts
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QMainWindow



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1128, 704)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(930, 600, 121, 20))
        self.Button1.setObjectName("Button1")
        self.Slider1 = QtWidgets.QSlider(self.centralwidget)
        self.Slider1.setGeometry(QtCore.QRect(270, 501, 481, 20))
        self.Slider1.setOrientation(QtCore.Qt.Horizontal)
        self.Slider1.setObjectName("Slider1")

        self.spinBox1 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox1.setGeometry(QtCore.QRect(940, 380, 42, 22))
        self.spinBox1.setObjectName("spinBox1")

        self.spinBox2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox2.setGeometry(QtCore.QRect(940, 410, 42, 22))
        self.spinBox2.setObjectName("spinBox2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 470, 55, 16))
        self.label.setObjectName("label")

        self.SpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.SpinBox.setGeometry(QtCore.QRect(940, 450, 91, 31))
        self.SpinBox.setObjectName("SpinBox")


        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(430, 200, 141, 21))
        self.Button2.setObjectName("Button2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 80, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(820, 380, 111, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(820, 410, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(820, 460, 111, 20))
        self.label_4.setObjectName("label_4")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(450, 530, 121, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1128, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Button2.clicked.connect(self.btn_help)
        self.Button1.clicked.connect(self.btn_Stop_handler)
        self.actionHelp.triggered.connect(self.btn_hjelps)
        #self.spinBox1.valueChanged.connect(self.spinBox_Displacement)
        #self.spinBox2.valueChanged.connect(self.spinBox_Time)
        self.SpinBox.valueChanged.connect(self.SpinBox_TotalDisp)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button1.setText(_translate("MainWindow", "Stop the system"))
        self.Slider1.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Extension"))
        self.Button2.setText(_translate("MainWindow", "Go to home position"))

        self.comboBox.setItemText(0, _translate("MainWindow", "Positioning Mode"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Operational Mode"))

        self.label_2.setText(_translate("MainWindow", "Displacement rate"))
        self.label_3.setText(_translate("MainWindow", "Time"))
        self.label_4.setText(_translate("MainWindow", "Total Displacement"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))

    def pop_window(self, text, title, over):

        msg = QtWidgets.QMessageBox()

        msg.setStandardButtons(QtWidgets.QMessageBox.Close)
        msg.setText("{}".format(text))
        #msg.setInformativeText('{}'.format(over))
        msg.setDetailedText('{}'.format(over))
        msg.setWindowTitle("{}".format(title))
        msg.resize()

        msg.exec_()

    #def btn_help(self):
       # self.pop_window('Her ska info komme!', 'Hjelp', 'Les nøye')

    def btn_Stop_handler(self):
        QtCore.QCoreApplication.instance().quit()

    def btn_help(self):
        Scripts.toekstra_forskjyv()

    def btn_hjelps(self):
        f = open('Filhandler.txt', 'r')
        if f.mode == 'r':
            contents = f.read()
        self.pop_window('Press Show details for more information','Georigg', contents)

    def SpinBox_TotalDisp(self):
        self.SpinBox.value()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
