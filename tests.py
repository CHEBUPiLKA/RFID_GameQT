import unittest
from Game_Classes.UTILITIES import UTILITIES
from Game_Classes.STATUS import STATUS


class GameTests(unittest.TestCase):
    def test_adding_quests(self):
        utils = UTILITIES()
        self.assertEqual(utils.addQuest(0xFAF, "Some objective", "Some description", STATUS.DOING), 1)


if __name__ == '__main__':
    unittest.main()
