import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "bcabc"
        ans = "abc"

        self.assertEqual(ans, self.s.removeDuplicateLetters(s))

    def test2(self):
        s = "cbacdcbc"
        ans = "acdb"

        self.assertEqual(ans, self.s.removeDuplicateLetters(s))

    def test3(self):
        s = "bbcaac"
        ans = "bac"

        self.assertEqual(ans, self.s.removeDuplicateLetters(s))


if __name__ == "__main__":
    unittest.main()
