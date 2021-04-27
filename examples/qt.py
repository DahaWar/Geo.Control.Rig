from serial import Serial
from PyQt5 import QtCore

from PyQt5 import QtWidgets
import sqlite3


class Ui_Form(object):

    def openwindow(self):

        self.window = QtWidgets.QMainWindow()

        self.ui.setupUi(self.window)
        self.window.show()
        Georigg.hide()

    def setupUi(self, Georigg):
        Georigg.setObjectName("GEORIGG")
        Georigg.resize(900, 600)

        self.gridLayoutWidget = QtWidgets.QWidget(Georigg)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")

<<<<<<< HEAD
=======
        '''self.l_username = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l_username.setObjectName("l_username")
        self.gridLayout.addWidget(self.l_username, 0, 0, 1, 1)

        self.l_password = QtWidgets.QLabel(self.gridLayoutWidget)
        self.l_password.setObjectName("l_password")
        self.gridLayout.addWidget(self.l_password, 1, 0, 1, 1)
'''
        '''self.txt_password = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_password.setObjectName("txt_password")
        self.gridLayout.addWidget(self.txt_password, 1, 1, 1, 1)'''

        '''self.txt_username = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_username.setObjectName("txt_username")
        self.gridLayout.addWidget(self.txt_username, 0, 1, 1, 1)
        '''
>>>>>>> de0d5fd2370a49cfa04b5248d4fe4fd102ef35de
        self.btn_help = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_help.setStyleSheet("background-color: rgb(27, 27, 27);\n"
                                    "color: \'white\';")
        self.btn_help.setObjectName("btn_help")
<<<<<<< HEAD
        self.gridLayout.addWidget(self.btn_help)
=======
        self.gridLayout.addWidget(self.btn_help, 3, 1, 1, 1)

>>>>>>> de0d5fd2370a49cfa04b5248d4fe4fd102ef35de
        self.btn_exit = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_exit.setStyleSheet("background-color: rgb(27, 27, 27);\n"
                                    "color: \'white\';")
        self.btn_exit.setObjectName("btn_exit")
<<<<<<< HEAD
        self.gridLayout.addWidget(self.btn_exit)
=======
        self.gridLayout.addWidget(self.btn_exit, 1, 1, 1, 1)
>>>>>>> de0d5fd2370a49cfa04b5248d4fe4fd102ef35de

        self.retranslateUi(Georigg)
        QtCore.QMetaObject.connectSlotsByName(Georigg)

        self.btn_exit.clicked.connect(self.btn_exit_handler)
        self.btn_help.clicked.connect(self.btn_help_handler)

    def retranslateUi(self, Georigg):
        _translate = QtCore.QCoreApplication.translate
        Georigg.setWindowTitle(_translate("Georigg", "Georigg"))
<<<<<<< HEAD
=======
        '''self.l_username.setText(_translate("Georigg", "HELP"))
        self.l_password.setText(_translate("Georigg", "Password"))'''
>>>>>>> de0d5fd2370a49cfa04b5248d4fe4fd102ef35de
        self.btn_help.setText(_translate("Georigg", "Help"))
        self.btn_exit.setText(_translate("Georigg", "Exit"))

    def pop_window(self, text):

        msg = QtWidgets.QMessageBox()

        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("{}".format(text))
        msg.setInformativeText('{}'.format(text))
        msg.setWindowTitle("{}".format(text))

        msg.exec_()

    def btn_exit_handler(self):
        self.openwindow()

<<<<<<< HEAD
    def btn_help_handler(self):
        if len(self.btn_help):
            self.pop_window('Enter Valid Data !')

        else:
            username = self.txt_username.text()
            password = self.txt_password.text()

            conn = sqlite3.connect('user.db')
            cursor = conn.cursor()

            cursor.execute("SELECT username,password FROM credentials")
            val = cursor.fetchall()

            if len(val) >= 1:

                for x in val:
                    if username in x[0] and password in x[1]:
                        print("welcome ")
                    else:
                        pass
            else:
                print('No user Found')
=======
    def btn_login_handler(self):

        self.pop_window('Enter Valid Data !')
>>>>>>> de0d5fd2370a49cfa04b5248d4fe4fd102ef35de


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()

    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

