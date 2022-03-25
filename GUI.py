from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
import sys
from GIF import Ui_MainWindow
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
def guiStartup():
    app = QApplication(sys.argv)
    win = Window()
    win.showFullScreen()
    sys.exit(app.exec())