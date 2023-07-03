import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        out = ["cats and dog", "cat sand dog"]
        self.assertEqual(self.s.wordBreak(s, wordDict), out)

    def test2(self):
        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
        out = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
        self.assertEqual(self.s.wordBreak(s, wordDict), out)

    def test3(self):
        s = "a"
        wordDict = ["a"]
        out = ["a"]
        self.assertEqual(self.s.wordBreak(s, wordDict), out)


if __name__ == "__main__":
    unittest.main()
