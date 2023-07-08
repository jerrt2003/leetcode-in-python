import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        out = 5
        self.assertEqual(self.s.ladderLength(beginWord, endWord, wordList), out)

    def test2(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        out = 0
        self.assertEqual(self.s.ladderLength(beginWord, endWord, wordList), out)


if __name__ == "__main__":
    unittest.main()
