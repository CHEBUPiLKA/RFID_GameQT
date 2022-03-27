import sqlite3 as sq
class DB:
    def __init__(self, database="players.sqlite"):
        self._db = sq.connect(database, check_same_thread=False)
        self._cur = self._db.cursor()
        self.init_uids = [i[0] for i in self._cur.execute("SELECT UID FROM Players").fetchall()]
        self._cur.close()
    def register(self, UID):
        try:
            self._cur = self._db.cursor()
            self._cur.execute("INSERT INTO Players (UID) VALUES ({})".format(UID))
            self._cur.close()
            return 1
        except Exception as e:
            return str(e)
    def getQuestData(self, QuestId):
        return "Data for quest id: {}".format(QuestId)