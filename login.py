# Copyrights to Suryansh Shakya

import os
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from PyQt5.QtWidgets import QMessageBox
import encrypt
import register
from pathlib import Path
from PyQt5.QtCore import QCoreApplication, Qt
import calendar

class Ui_login(object):
        def setupUi(self, login):
                login.setObjectName("login")
                login.resize(330, 450)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(login.sizePolicy().hasHeightForWidth())
                login.setSizePolicy(sizePolicy)
                login.setMinimumSize(QtCore.QSize(330, 450))
                login.setMaximumSize(QtCore.QSize(330, 450))
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/bckg/pics/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                login.setWindowIcon(icon)
                login.setStyleSheet("")
                self.centralwidget = QtWidgets.QWidget(login)
                self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
                self.centralwidget.setObjectName("centralwidget")
                self.bckgrnd = QtWidgets.QGraphicsView(self.centralwidget)
                self.bckgrnd.setGeometry(QtCore.QRect(0, 0, 330, 450))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.bckgrnd.sizePolicy().hasHeightForWidth())
                self.bckgrnd.setSizePolicy(sizePolicy)
                self.bckgrnd.setMaximumSize(QtCore.QSize(330, 450))
                self.bckgrnd.setAutoFillBackground(True)
                self.bckgrnd.setStyleSheet("background-image: url(:/bckg/pics/bck.png);\n"
        "background-color: rgb(0, 48, 58);")
                self.bckgrnd.setObjectName("bckgrnd")
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(90, 260, 161, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton.setFont(font)
                self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
        "    color:rgba(255,255,255,210);\n"
        "    border-radius:5px;\n"
        "}\n"
        "QPushButton#pushButton:hover{\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 64, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
        "}\n"
        "QPushButton#pushButton:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(105,118,132,200);\n"
        "}")
                self.pushButton.setObjectName("pushButton")
                self.pushButton.clicked.connect(self.btn_clicked)
                self.frgt_pass = QtWidgets.QPushButton(self.centralwidget,clicked= lambda:self.forget())
                self.frgt_pass.setGeometry(QtCore.QRect(90, 350, 161, 17))
                self.frgt_pass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.frgt_pass.setStyleSheet("background-color: rgb(0,0,0,0);\n"
        "color:rgba(255,255,255,200);\n"
        "border: none;")
                self.frgt_pass.setObjectName("frgt_pass")
                self.username = QtWidgets.QLineEdit(self.centralwidget)
                self.username.setGeometry(QtCore.QRect(90, 130, 161, 41))
                self.username.setStyleSheet("background-color: rgb(0,0,0,0);\n"
        "border: none;\n"
        "border-bottom:2px solid rgba(255,255, 255 255);\n"
        "color:rgba(255,255,255,230);\n"
        "padding-bottom:7px;")
                self.username.setText("")
                self.username.setObjectName("username")
                self.password = QtWidgets.QLineEdit(self.centralwidget)
                self.password.setGeometry(QtCore.QRect(90, 190, 161, 41))
                self.password.setStyleSheet("background-color: rgb(0,0,0,0);\n"
        "border: none;\n"
        "border-bottom:2px solid rgba(255,255, 255 255);\n"
        "color:rgba(255,255,255,230);\n"
        "padding-bottom:7px;")
                self.password.setText("")
                self.password.setEchoMode(QtWidgets.QLineEdit.Password)
                self.password.setObjectName("password")
                self.sign_up = QtWidgets.QPushButton(self.centralwidget,clicked= lambda:self.openwindow())
                self.sign_up.setGeometry(QtCore.QRect(120, 320, 89, 25))
                self.sign_up.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.sign_up.setStyleSheet("background-color: rgb(0,0,0,0);\n"
        "color:rgba(255,255,255,200);\n"
        "border: none;")
                self.sign_up.setObjectName("sign_up")
                login.setCentralWidget(self.centralwidget)

                self.retranslateUi(login)
                QtCore.QMetaObject.connectSlotsByName(login)

#opens register window
        def openwindow(self):
                self.window = QtWidgets.QMainWindow()
                self.ui = register.Ui_sign_up()
                self.ui.setupUi(self.window)
                self.window.show()

#logs in user
        def btn_clicked(self):
                path = Path("storage/users/"+self.username.text())
                msg = QMessageBox()
                self.user = self.username.text()
                self.pwd = self.password.text()
                if self.user == "" or self.pwd == "":
                        msg.setWindowTitle("Error")
                        msg.setText("Please enter username or password")
                        msg.setIcon(QMessageBox.Warning)
                        msg.exec_()
                else:
                        if os.path.isdir(path):
                                pass_dir = Path("storage/users/"+self.username.text()+"/pass.txt")
                                with open(pass_dir,encoding="utf-8") as pass_obj:
                                        pass_txt = pass_obj.read()
                                        pass_txt = encrypt.decrypt(pass_txt)
                                if self.pwd == pass_txt:
                                        self.window = QtWidgets.QMainWindow()
                                        self.ui = calendar.Ui_MainWindow()
                                        self.ui.setupUi(self.window,self.user)
                                        self.window.show()
                                        login.close()
                                        
                                        
                                else:
                                        msg.setWindowTitle("Error")
                                        msg.setText("Wrong password")
                                        msg.setIcon(QMessageBox.Warning)
                                        msg.exec_()

                        else:
                                msg.setWindowTitle("Error")
                                msg.setText("Wrong user name or password")
                                msg.setIcon(QMessageBox.Warning)
                                msg.exec_()

        def forget(self):
                msg = QMessageBox()
                msg.setWindowTitle("Information")
                msg.setText("Feature under development")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()

        def retranslateUi(self, login):
                _translate = QtCore.QCoreApplication.translate
                login.setWindowTitle(_translate("login", "Login"))
                self.pushButton.setText(_translate("login", "Log In"))
                self.frgt_pass.setText(_translate("login", "Forgot your password?"))
                self.username.setPlaceholderText(_translate("login", "Username"))
                self.password.setPlaceholderText(_translate("login", "Password"))
                self.sign_up.setText(_translate("login", "Sign Up"))


import ediary_rc #contains resource file for the design of form


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())

