# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GIF.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        #self.label.setMinimumSize(QtCore.QSize(1920, 1080))
        #self.label.setMaximumSize(QtCore.QSize(1920, 1080))
        #self.label.setScaledContents(True)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.label.cursor()
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 500, 1920, 1080))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.label_2.cursor()
        self.label_2.setObjectName("label_2")
        self.set_color()
        self.label_2.setText('<h4 style="color: rgb(255, 255, 255);">YOU ARE NOT REGISTERED, PLEASE CONTACT MAKSIM IVANOV</h4>')
        self.label_2.setFont(QtGui.QFont("Times", 40, QtGui.QFont.Bold))
        self.label_2.adjustSize()
        self.label_2.hide()

        MainWindow.setCentralWidget(self.centralwidget)
        self.app = QtWidgets.QApplication(sys.argv)
        self.screen = self.app.primaryScreen()
        self.size = self.screen.size()
        self.movie = QMovie("Portal2.gif")
        #self.movie.setScaledSize(QtCore.QSize(1920, 1080))
        self.movie.setScaledSize(QtCore.QSize(self.size.width(), self.size.height()))
        self.label.setMovie(self.movie)
        self.movie.start()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
