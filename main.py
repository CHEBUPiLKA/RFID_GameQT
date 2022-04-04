import sys
from pirc522 import RFID
import threading
from os import system
from GUI import guiStartup, guiQuest, cardAuth
from Game_Classes.UTILITIES import UTILITIES
from Game_Classes.PLAYER import PLAYER
from Game_Classes.QUEST import QUEST
from time import sleep
from random import choice

rdr = RFID()
ut = UTILITIES()

master_UID = 1863213129237

QuestsIDS = ut.initQuests()
PlayersIDS = ut.initPlayers()
Quests = []
Players = []


def RFIDScan():
    while True:
        rdr.wait_for_tag()
        (error, tag_type) = rdr.request()
        if not error:
            (error, uid) = rdr.anticoll()
            if not error:
                uid = int("".join(list(map(str, uid))))
                if uid == master_UID:
                    print("REGISTRATION PROCESS INIT")
                    sleep(2)
                    print("Please be ready to scan player card in 2 seconds")
                    sleep(2)
                    rdr.wait_for_tag()
                    (error, tag_type) = rdr.request()
                    if not error:
                        print("REGISTRATING...")
                        (error, uid_new) = rdr.anticoll()
                        if not error:
                            uid_new = int("".join(list(map(str, uid_new))))
                            print("UID: " + str(uid_new))
                            if db.register(uid_new) == 1:
                                PlayersIDS.append(uid_new)
                                print("DONE")
                                sleep(2)
                            else:
                                print("ERROR REGISTRATING")
                                sleep(2)
                elif uid not in PlayersIDS:
                    cardAuth()
                else:
                    player = PLAYER(uid)
                    quest = QUEST(choice(QuestsIDS))
                    quest.assignQuest(player)
                    guiQuest(quest)


if __name__ == "__main__":
    t = threading.Thread(target=RFIDScan)
    t.start()
    guiStartup()
