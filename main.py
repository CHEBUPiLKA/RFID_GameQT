from DBControl import DB
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from GIF import Ui_MainWindow
from multiprocessing import Process
from time import sleep
db = DB()

Users = db.init_uids

def RFIDScan():
    while True:
        print("dsad")
        sleep(1)

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
t = Process(target=RFIDScan)
t.start()
app = QApplication(sys.argv)
win = Window()
win.showFullScreen()
sys.exit(app.exec())