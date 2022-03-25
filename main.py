from DBControl import DB
import sys
from pirc522 import RFID
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from GIF import Ui_MainWindow
from multiprocessing import Process
from time import sleep
rdr = RFID()
db = DB()

Users = db.init_uids

def RFIDScan():
    while True:
        rdr.wait_for_tag()
        (error, tag_type) = rdr.request()
        if not error:
            print("Tag detected")
            (error, uid) = rdr.anticoll()
            if not error:
                print("UID: " + str(uid))
                uid = int("".join(list(map(str, uid))))
                if uid not in Users:
                    print("You are not registered, do you want to register[Y/N]?")
                    if input().lower() == 'y':
                        print("Registering...")
                        if db.register(uid) == 1:
                            Users.append(uid)
                            print("DONE")
                        else:
                            print("ERROR REGISTERING")
                else:
                    print("Hello! You authed!")
                    sleep(2)

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