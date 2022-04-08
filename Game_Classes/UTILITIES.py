import sqlite3 as sq
from Game_Classes.STATUS import STATUS

class UTILITIES:
    def __init__(self):
        self._db = sq.connect("players.sqlite", check_same_thread=False)
        self._cur = self._db.cursor()
        self._playerUIDS = [i[0] for i in self._cur.execute("SELECT UID FROM Players").fetchall()]
        self._questIDS = [i[0] for i in self._cur.execute("SELECT Id FROM Quests").fetchall()]
        self._cur.close()

    def initPlayers(self):
        return self._playerUIDS

    def initQuests(self):
        return self._questIDS

    def registerPlayer(self, UID):
        try:
            self._cur = self._db.cursor()
            self._cur.execute("INSERT INTO Players (UID) VALUES ({})".format(UID))
            self._cur.close()
            self._db.commit()
            return 1
        except Exception as e:
            return str(e)

    def addQuest(self, quest_id: int, objective: str, description: str, status: STATUS, exp: int = 200):
        try:
            self._cur = self._db.cursor()
            self._cur.execute("INSERT INTO Quests "
                              "(Id, Objective, Description, Status, AwardEXP) "
                              "VALUES ({}, '{}', '{}', {}, {});"
                              .format(quest_id, objective, description, int(status), exp))
            self._cur.close()
            self._db.commit()
            self._questIDS.append(quest_id)
            return 1
        except Exception as e:
            return str(e)

