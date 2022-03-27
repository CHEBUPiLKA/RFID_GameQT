from DBControl import DB
import sys
from pirc522 import RFID
from multiprocessing import Process
from GUI import guiStartup
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
if __name__ == "__main__":
    t = Process(target=RFIDScan)
    t.start()
    guiStartup()