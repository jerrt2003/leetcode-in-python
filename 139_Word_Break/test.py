import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        self.assertTrue(self.s.wordBreak(s, wordDict))


if __name__ == "__main__":
    unittest.main()
