# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JarvisUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JarvisGUI(object):
    def setupUi(self, JarvisGUI):
        JarvisGUI.setObjectName("JarvisGUI")
        JarvisGUI.resize(2032, 1006)
        self.centralwidget = QtWidgets.QWidget(JarvisGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-220, 50, 2031, 1001))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/7LP8.gif"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1600, 880, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Orator Std")
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1740, 880, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Orator Std")
        font.setPointSize(36)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 110, 401, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/T8bahf.gif"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1510, 0, 521, 1001))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Images/side.PNG"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(6, -18, 1511, 121))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Images/bottom.PNG"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 2, 81, 1001))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Images/side.PNG"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1125, 20, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro Light")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1470, 20, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro Light")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 590, 381, 261))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("background:transparent;")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("Images/logo jarvis.gif"))
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_4.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        self.label_7.raise_()
        JarvisGUI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(JarvisGUI)
        self.statusbar.setObjectName("statusbar")
        JarvisGUI.setStatusBar(self.statusbar)

        self.retranslateUi(JarvisGUI)
        QtCore.QMetaObject.connectSlotsByName(JarvisGUI)

    def retranslateUi(self, JarvisGUI):
        _translate = QtCore.QCoreApplication.translate
        JarvisGUI.setWindowTitle(_translate("JarvisGUI", "J.A.R.V.I.S"))
        self.pushButton.setText(_translate("JarvisGUI", "RUN"))
        self.pushButton_2.setText(_translate("JarvisGUI", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JarvisGUI = QtWidgets.QMainWindow()
    ui = Ui_JarvisGUI()
    ui.setupUi(JarvisGUI)
    JarvisGUI.show()
    sys.exit(app.exec_())
