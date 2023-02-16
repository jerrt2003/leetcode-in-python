import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        ans = [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
        self.assertEqual(ans, self.s.findLadders(beginWord, endWord, wordList))

    def test2(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
        ans = []
        self.assertEqual(ans, self.s.findLadders(beginWord, endWord, wordList))        

if __name__ == "__main__":
    unittest.main()