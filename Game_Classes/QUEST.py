import sqlite3 as sq

class QUEST:
    def __init__(self, ID):
        self._player = None
        self._db = sq.connect("../players.sqlite", check_same_thread=False)
        self._cur = self._db.cursor()
        self._data = [i[0] for i in self._cur.execute(f"SELECT * FROM Quests WHERE Id={ID}").fetchall()]
        self._id = self._data[0]
        self._objective = self._data[1]
        self._description = self._data[2]
        self._status = self._data[3]
        self._EXP = self._data[4]
        self._cur.close()
        self._db.close()

    def setStatus(self, status):
        self._status = status
        self._db = sq.connect("players.sqlite", check_same_thread=False)
        self._cur = self._db.cursor()
        self._cur.execute(f"UPDATE Quests SET Status = {status} WHERE Id = {self._id}")
        self._cur.close()
        self._db.commit()
        self._db.close()
        if status == 2:
            self.__assignAward()

    def getObjective(self):
        return self._objective

    def getDescription(self):
        return self._description

    def getStatus(self):
        return self._status

    def getId(self):
        return self._id

    def getExp(self):
        return self._EXP

    def assignQuest(self, player):
        self._player = player
        player.setQuest(self._id)

    def __assignAward(self):
        self._player._setEXP(self._EXP)
