# Copyrights to Suryansh Shakya

import os
from pathlib import Path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox,QAction
import datetime
import encrypt
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,date,user):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setMinimumSize(QtCore.QSize(500, 600))
        MainWindow.setMaximumSize(QtCore.QSize(500, 600))
        MainWindow.setStyleSheet("")



        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 500, 600))
        self.graphicsView.setStyleSheet("background-image: url(:/background/pics/diary.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(90, 100, 321, 421))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setStatusTip('About')
        self.actionAbout.triggered.connect(self.about)
        self.menuAbout.addAction(self.actionAbout)

        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.setStatusTip('Save File')
        self.actionSave.triggered.connect(self.file_save)

        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.exit)
        self.menufile.addAction(self.actionSave)
        self.menufile.addAction(self.actionExit)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        #to be changes further
        self.date = date
        self.user = user
        self.year = str(date.year())
        self.month = str(date.month())
        self.day = str(date.day())
        self.dir = Path("storage/users/"+self.user+"/"+self.year+"/"+self.month+"/")
        if not os.path.isdir(self.dir):
            os.makedirs(self.dir)
        
        self.file_dir = Path("storage/users/"+self.user+"/"+self.year+"/"+self.month+"/"+self.day+".txt")
        if os.path.isfile(self.file_dir):
            self.read()
        else:
            self.setDate()
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def about(self):
        msg = QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("Made by Suryansh Shakya")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
    def read(self):
        dir = Path("storage/users/"+self.user+"/"+self.year+"/"+self.month+"/"+self.day+".txt")
        with open(dir,encoding="utf-8") as pass_obj:
            page_txt = pass_obj.read()
            page_txt = encrypt.decrypt(page_txt)
        self.plainTextEdit.insertPlainText(page_txt)

    def setDate(self):
        today = datetime.datetime.now()
        str_date = str(self.date.day())
        str_time = str(today.strftime('%I %p'))
        str_month = str(self.date.month())
        str_year = str(self.date.year())
        str_wday = str(today.strftime('%A'))
        self.plainTextEdit.insertPlainText(str_date+"/"+str_month+"/"+str_year+"\n"+str_wday+"\n"+str_time+"\n\nDear Diary\n\n\t")
    
    def file_save(self):
        msg = QMessageBox()
        wdir = Path("storage/users/"+self.user+"/"+self.year+"/"+self.month+"/"+self.day+".txt")
        encr_txt = encrypt.encrypt(self.plainTextEdit.toPlainText())
        try:
            with open(wdir,'w',encoding="utf-8") as userfile:
                userfile.write(encr_txt)
        except:
            msg.setWindowTitle("Error")
            msg.setText("Could not save the page")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        else:
            msg.setWindowTitle("Success")
            msg.setText("Page Saved")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

    def exit(self):
        sys.exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Diary"))
        self.menufile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "Info"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
    

import diary_rc


    

