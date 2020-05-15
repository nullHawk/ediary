# Copyrights to Suryansh Shakya

from PyQt5 import QtCore, QtGui, QtWidgets
import diary


class Ui_MainWindow(object):

    def open_diary(self,date):
        self.window = QtWidgets.QMainWindow()
        self.ui = diary.Ui_MainWindow()
        self.ui.setupUi(self.window,date,self.user)
        self.window.show()

    def setupUi(self, MainWindow,user):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/bck/pics/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 700, 500))
        self.graphicsView.setStyleSheet("background-image: url(:/bck/pics/calendar.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(63, 90, 576, 321))
        self.calendarWidget.setStyleSheet("selection-background-color: rgb(71, 145, 168);\n"
"gridline-color: rgb(60, 144, 165);")
        self.calendarWidget.setObjectName("calendarWidget")

        self.calendarWidget.activated.connect(self.open_diary)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 60, 300, 31))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Purisa\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.user = user

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calendar"))
        self.label.setText(_translate("MainWindow", "Choose your Date"))
    
    

import calender_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

