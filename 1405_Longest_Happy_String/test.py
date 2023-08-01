import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        a = 1
        b = 1
        c = 7
        ans = "ccaccbcc"
        self.assertEqual(ans, self.s.longestDiverseString(a, b, c))

    def test2(self):
        a = 7
        b = 1
        c = 0
        ans = "aabaa"
        self.assertEqual(ans, self.s.longestDiverseString(a, b, c))

    def test3(self):
        a = 0
        b = 8
        c = 11
        ans = "ccbccbbccbbccbbccbc"
        self.assertEqual(ans, self.s.longestDiverseString(a, b, c))


if __name__ == "__main__":
    unittest.main()
