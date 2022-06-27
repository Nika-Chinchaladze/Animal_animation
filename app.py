from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 606)
        MainWindow.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tiger = QtWidgets.QPushButton(self.centralwidget)
        self.tiger.setGeometry(QtCore.QRect(30, 330, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tiger.setFont(font)
        self.tiger.setStyleSheet("gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tiger.setObjectName("tiger")
        self.wolf = QtWidgets.QPushButton(self.centralwidget)
        self.wolf.setGeometry(QtCore.QRect(200, 330, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wolf.setFont(font)
        self.wolf.setStyleSheet("gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.wolf.setObjectName("wolf")
        self.panter = QtWidgets.QPushButton(self.centralwidget)
        self.panter.setGeometry(QtCore.QRect(370, 330, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.panter.setFont(font)
        self.panter.setStyleSheet("gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.panter.setObjectName("panter")
        self.bear = QtWidgets.QPushButton(self.centralwidget)
        self.bear.setGeometry(QtCore.QRect(110, 410, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bear.setFont(font)
        self.bear.setStyleSheet("gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.bear.setObjectName("bear")
        self.monkey = QtWidgets.QPushButton(self.centralwidget)
        self.monkey.setGeometry(QtCore.QRect(280, 410, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.monkey.setFont(font)
        self.monkey.setStyleSheet("gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.monkey.setObjectName("monkey")
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(190, 490, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.close.setFont(font)
        self.close.setStyleSheet("gridline-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.close.setObjectName("close")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 461, 291))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("vs code files/tiger.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tiger.clicked.connect(self.show_tiger)
        self.wolf.clicked.connect(self.show_wolf)
        self.panter.clicked.connect(self.show_panter)
        self.bear.clicked.connect(self.show_bear)
        self.monkey.clicked.connect(self.show_monkey)
        self.close.clicked.connect(MainWindow.close)
    
    def show_tiger(self):
        self.label.setPixmap(QtGui.QPixmap("tiger.jpg"))
    def show_wolf(self):
        self.label.setPixmap(QtGui.QPixmap("wolf.jpg"))
    def show_panter(self):
        self.label.setPixmap(QtGui.QPixmap("panter.jpg"))
    def show_bear(self):
        self.label.setPixmap(QtGui.QPixmap("bear.jpg"))
    def show_monkey(self):
        self.label.setPixmap(QtGui.QPixmap("monkey.jpg"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tiger.setText(_translate("MainWindow", "Tiger"))
        self.wolf.setText(_translate("MainWindow", "Wolf"))
        self.panter.setText(_translate("MainWindow", "Black Panter"))
        self.bear.setText(_translate("MainWindow", "Bear"))
        self.monkey.setText(_translate("MainWindow", "Monkey"))
        self.close.setText(_translate("MainWindow", "CLOSE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
