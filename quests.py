from Game_Classes import UTILITIES
import sys
import sqlite3 as sql

def printQuests():
	db = sql.connect('players.sqlite', check_same_thread=False)
	cur = db.cursor()
	for q in cur.execute('SELECT * FROM Quests').fetchall():
		print('Quest "{}" with ID {}'.format(q[1], q[0]))
		print('Description: {}'.format(q[2]))
		print('Status: {}'.format(q[3]))
		print('Award EXP: {}'.format(q[4]))
		print('============================')

def registerQuestsLegacy():
    utils = UTILITIES.UTILITIES()
    qid = int(input("Input quest id: "))
    name = input("Input quest name: ")
    desc = input("Input quest description: ")
    exp = int(input("Input quest exp award: "))
    utils.addQuest(qid, name, desc, 0, exp)

def registerQuests():
    utils = UTILITIES.UTILITIES()
    GLOBAL_QUEST_ID = 0xA000
    print("Registering quests! Press CTRL+C to exit")
    while True:
        qstr = input("Enter quest data: ").split("@")
        name = qstr[0]
        desc = qstr[1]
        if len(qstr) > 2:
            exp = qstr[2]
            qid = qstr[3]
        else:
            exp = 200
            qid = GLOBAL_QUEST_ID + 1
            GLOBAL_QUEST_ID = GLOBAL_QUEST_ID + 1
        utils.addQuest(qid, name, desc, 0, exp)

def deleteQuests():
    db = sql.connect('players.sqlite', check_same_thread=False)
    cur = db.cursor()
    print("Deleting quests! Enter quest ids to be deleted, or CTRL-C to exit!")
    while True:
        qid = int(input())
        cur.execute("DELETE FROM Quests WHERE Id={}".format(qid))
        db.commit()
    
    cur.close()
    db.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError("Expected mode! -r/-ws/-w")
    mode = sys.argv[1]
    if mode == "--read" or mode == "-r":
        printQuests()
    elif mode == "--write-single" or mode == "-ws":
        registerQuestsLegacy()
    elif mode == "--write" or mode == "-w":
        registerQuests()
    elif mode == "--delete" or mode == "-d":
        deleteQuests()
