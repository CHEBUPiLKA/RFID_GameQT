from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt, QPropertyAnimation, QSequentialAnimationGroup
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QColor, QPalette
import sys
import threading
from GIF import Ui_MainWindow
from time import sleep


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._color = None
        self.setupUi(self)
        self.animation = QPropertyAnimation(self)
        self.animation.setTargetObject(self.label)
        self.animation.setPropertyName(b'geometry')
        self.animation.setDuration(1000)
        self.animation.setStartValue(QtCore.QRect(0, 0, self.size().width(), self.size().height()))
        self.animation.setEndValue(QtCore.QRect(self.size().width() // 2, self.size().height() // 2, 0, 0))

        self.anim_2 = QPropertyAnimation(self)
        self.anim_2.setTargetObject(self.label_2)
        self.anim_2.setPropertyName(b'geometry')
        self.anim_2.setDuration(500)
        self.anim_2.setStartValue(QtCore.QRect(120, 0, 0, 0))
        self.anim_2.setEndValue(QtCore.QRect(120, 0, 1920, 1080))
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.animation)
        self.anim_group.addAnimation(self.anim_2)

    def set_color(self, col=(0, 0, 0)):
        self._color = QColor(col[0], col[1], col[2])
        self.setStyleSheet(
            'background-color: rgb({}, {}, {})'.format(self._color.red(), self._color.green(), self._color.blue()))

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_1:
            self.movie.stop()
        elif e.key() == Qt.Key_2:
            self.movie.start()
        elif e.key() == Qt.Key_3:
            self.label.hide()
        elif e.key() == Qt.Key_4:
            self.label.showNormal()
        elif e.key() == Qt.Key_5:
            self.label_2.showNormal()
        elif e.key() == Qt.Key_6:
            self.label_2.hide()
        elif e.key() == Qt.Key_7:
            self.animation.start()
        elif e.key() == Qt.Key_8:
            self.label.setGeometry(QtCore.QRect(0, 0, self.size().width(), self.size().height()))
        elif e.key() == Qt.Key_9:
            self.regRequest()
        elif e.key() == Qt.Key_0:
            cardAuth()

    def restoreDefault(self):
        self.label_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label.setGeometry(QtCore.QRect(0, 0, self.size().width(), self.size().height()))

    def regRequest(self):
        self.anim_group.start()

    def showQuest(self):
        pass


app = QApplication(sys.argv)
win = Window()

def guiStartup():
    win.showFullScreen()
    sys.exit(app.exec())


def cardAuth():
    win.regRequest()
    print("back here")


def guiQuest(quest):
    pass
