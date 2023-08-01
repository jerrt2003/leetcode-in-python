import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        words = ["a", "b", "ba", "bca", "bda", "bdca"]
        ans = 4
        self.assertEqual(ans, self.s.longestStrChain(words))

    def test2(self):
        words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
        ans = 5
        self.assertEqual(ans, self.s.longestStrChain(words))

    def test3(self):
        words = ["abcd", "dbqca"]
        ans = 1
        self.assertEqual(ans, self.s.longestStrChain(words))

    def test4(self):
        words = ["a", "ab", "ac", "bd", "abc", "abd", "abdd"]
        ans = 4
        self.assertEqual(ans, self.s.longestStrChain(words))


if __name__ == "__main__":
    unittest.main()
