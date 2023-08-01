import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "aaab"
        ans = ""
        self.assertEqual(ans, self.s.reorganizeString(s))

    def test2(self):
        s = "aaaaa"
        ans = ""
        self.assertEqual(ans, self.s.reorganizeString(s))

    def test3(self):
        s = "aab"
        ans = "aba"
        self.assertEqual(ans, self.s.reorganizeString(s))


if __name__ == "__main__":
    unittest.main()
