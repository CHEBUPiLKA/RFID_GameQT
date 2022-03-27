from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QColor
import sys
from GIF import Ui_MainWindow
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.animation = QPropertyAnimation(self)
        self.animation.setTargetObject(self.label)
        self.animation.setPropertyName(b'geometry')
        self.animation.setDuration(1000)
        self.animation.setStartValue(QtCore.QRect(0, 0, 1920, 1080))
        self.animation.setEndValue(QtCore.QRect(960, 540, 0, 0))

    def set_color(self, col=(0, 0, 0)):
        self._color = QColor(col[0], col[1], col[2])
        self.setStyleSheet('background-color: rgb({}, {}, {})'.format(self._color.red(), self._color.green(), self._color.blue()))
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
def guiStartup():
    app = QApplication(sys.argv)
    win = Window()
    win.showFullScreen()
    sys.exit(app.exec())