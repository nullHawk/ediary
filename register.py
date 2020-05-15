# Copyrights to Suryansh Shakya

from distutils.command import register
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from pathlib import Path
import os
import encrypt


class Ui_sign_up(object):
        def setupUi(self, sign_up):


                sign_up.setObjectName("sign_up")
                sign_up.resize(600, 700)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(sign_up.sizePolicy().hasHeightForWidth())
                sign_up.setSizePolicy(sizePolicy)
                sign_up.setMinimumSize(QtCore.QSize(600, 700))
                sign_up.setMaximumSize(QtCore.QSize(600, 700))
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/bckground/pics/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                sign_up.setWindowIcon(icon)
                self.centralwidget = QtWidgets.QWidget(sign_up)
                self.centralwidget.setObjectName("centralwidget")
                self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
                self.graphicsView.setGeometry(QtCore.QRect(0, 0, 600, 700))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
                self.graphicsView.setSizePolicy(sizePolicy)
                self.graphicsView.setMinimumSize(QtCore.QSize(600, 700))
                self.graphicsView.setMaximumSize(QtCore.QSize(600, 700))
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(75)
                self.graphicsView.setFont(font)
                self.graphicsView.setStyleSheet("background-image: url(:/bckground/pics/reg_bck.png);")
                self.graphicsView.setObjectName("graphicsView")
                self.username = QtWidgets.QLineEdit(self.centralwidget)
                self.username.setGeometry(QtCore.QRect(140, 230, 321, 51))
                self.username.setStyleSheet("background-color: rgb(0,0,0,0);\n"
        "color: rgb(98, 98, 98);\n"
        "font: 13pt \"Ubuntu\";\n"
        "border: none;\n"
        "border-bottom:2px solid rgba(150,150, 150 255);\n"
        "padding-bottom:7px;")
                self.username.setObjectName("username")
                self.password = QtWidgets.QLineEdit(self.centralwidget)
                self.password.setGeometry(QtCore.QRect(140, 310, 321, 51))
                self.password.setStyleSheet("background-color: rgb(0,0,0,0);\n"
        "color: rgb(98, 98, 98);\n"
        "font: 13pt \"Ubuntu\";\n"
        "border: none;\n"
        "border-bottom:2px solid rgba(150,150, 150 255);\n"
        "padding-bottom:7px;")
                self.password.setObjectName("password")
                self.email = QtWidgets.QLineEdit(self.centralwidget)
                self.email.setGeometry(QtCore.QRect(140, 390, 321, 51))
                self.email.setStyleSheet("background-color: rgb(0,0,0,0);\n"
        "color: rgb(98, 98, 98);\n"
        "font: 13pt \"Ubuntu\";\n"
        "border: none;\n"
        "border-bottom:2px solid rgba(150,150, 150 255);\n"
        "padding-bottom:7px;")
                self.email.setObjectName("email")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(200, 520, 201, 51))
                font = QtGui.QFont()
                font.setPointSize(18)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton.setFont(font)
                self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
        "    background-color: qlineargradient(spread:pad, x1:0.089, y1:0.534, x2:1, y2:0.546, stop:0 rgba(120, 82, 130, 255), stop:1 rgba(245, 183, 210, 255));\n"
        "    color:rgba(255,255,255,255);\n"
        "    border-radius:5px;\n"
        "}\n"
        "QPushButton#pushButton:hover{\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(140, 102, 150, 255), stop:1 rgba(255, 203, 230, 255));\n"
        "}\n"
        "QPushButton#pushButton:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(245,183,210,255);\n"
        "}")
                self.pushButton.setObjectName("pushButton")
                self.pushButton.clicked.connect(self.register)
                sign_up.setCentralWidget(self.centralwidget)

                self.retranslateUi(sign_up)
                QtCore.QMetaObject.connectSlotsByName(sign_up)
        def create_user(self,user,pwd,mail):
                encr_user=encrypt.encrypt(user)
                encr_pass=encrypt.encrypt(pwd)
                encr_email=encrypt.encrypt(mail)
                msg = QMessageBox()
                path = Path("storage/users/"+user+'/')
                user_path = Path("storage/users/"+user+'/user.txt')
                pass_path = Path("storage/users/"+user+'/pass.txt')
                email_path = Path("storage/users/"+user+'/email.txt')
                if not os.path.isdir(path):
                        os.makedirs(path)
                        open(user_path,'x')
                        open(pass_path,'x')
                        open(email_path,'x')

                        with open(user_path,'w',encoding="utf-8") as userfile:
                                userfile.write(encr_user)
                        with open(pass_path,'w',encoding="utf-8") as userfile:
                                userfile.write(encr_pass)
                        with open(email_path,'w',encoding="utf-8") as userfile:
                                userfile.write(encr_email)
                        msg.setWindowTitle("Success")
                        msg.setText("User created succesfully")
                        msg.setIcon(QMessageBox.Information)
                        msg.exec_()
                else:
                        msg.setWindowTitle("Error")
                        msg.setText("User already exists")
                        msg.setIcon(QMessageBox.Warning)
                        msg.exec_()


                pass

        def register(self):
                msg = QMessageBox()
                if self.username.text() == "" or self.password.text() == "" or self.email.text() == "":
                        msg.setWindowTitle("Error")
                        msg.setText("Please fill all the fields")
                        msg.setIcon(QMessageBox.Warning)
                        msg.exec_()
                elif '@' not in self.email.text():
                        msg.setWindowTitle("Error")
                        msg.setText("Enter valid email")
                        msg.setIcon(QMessageBox.Warning)
                        msg.exec_()
                else:
                        self.create_user(self.username.text(), self.password.text(), self.email.text())
        def retranslateUi(self, sign_up):
                _translate = QtCore.QCoreApplication.translate
                sign_up.setWindowTitle(_translate("sign_up", "Sign Up"))
                self.username.setPlaceholderText(_translate("sign_up", "Username"))
                self.password.setPlaceholderText(_translate("sign_up", "Password"))
                self.email.setPlaceholderText(_translate("sign_up", "Email"))
                self.pushButton.setText(_translate("sign_up", "Sign Up"))
import register_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sign_up = QtWidgets.QMainWindow()
    ui = Ui_sign_up()
    ui.setupUi(sign_up)
    sign_up.show()
    sys.exit(app.exec_())

