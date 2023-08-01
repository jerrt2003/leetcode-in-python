import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "abcxyz123"
        words = ["abc", "123"]
        self.assertEqual("<b>abc</b>xyz<b>123</b>", self.s.addBoldTag(s, words))

    def test2(self):
        s = "aaabbcc"
        words = ["aaa", "aab", "bc"]
        self.assertEqual("<b>aaabbc</b>c", self.s.addBoldTag(s, words))


if __name__ == "__main__":
    unittest.main()
