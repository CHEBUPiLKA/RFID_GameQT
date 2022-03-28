from DBControl import DB
import sys
from pirc522 import RFID
from random import choice
from time import sleep
from os import system
rdr = RFID()
db = DB()

master_UID = 0

Users = db.init_uids

def getRandomQuest():
    f = open("Quests.txt", 'r')
    quests = f.readlines()

    #(Objective, Description, status)
    #------------------------ 0 - Active, 1 - Taken, 2 - Done
    quests = [(i.split('@')[0], i.split('@')[1], i.split('@')[2]) for i in quests]
    return choice(quests)

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
                    print("You are not registered, please contact Maksim Ivanov")
                elif uid == master_UID:
                    print("REGISTRATION PROCESS INIT")
                    print("Please scan player card")
                    rdr.wait_for_tag()
                    (error, tag_type) = rdr.request()
                    if not error:
                        print("REGISTRATING...")
                        (error, uid_new) = rdr.anticoll()
                        if not error:
                            print("UID: " + str(uid_new))
                            uid_new = int("".join(list(map(str, uid_new))))
                            if db.register(uid_new) == 1:
                                Users.append(uid_new)
                                print("DONE")
                            else:
                                print("ERROR REGISTRATING")
                else:
                    print("Hello! You authed!")
                    sleep(1)
                    system("clear")
                    q = getRandomQuest()
                    print(f"YOUR QUEST FOR TODAY IS: \t {q[0]}\n\n\nDESCRIPTION: \t {q[1]}")
                    sleep(5)
if __name__ == "__main__":
    RFIDScan()