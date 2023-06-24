import unittest

from solution3 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "eceba"
        k = 2
        ans = 3
        self.assertEqual(ans, self.s.lengthOfLongestSubstringKDistinct(s, k))

    def test2(self):
        s = "aa"
        k = 1
        ans = 2
        self.assertEqual(ans, self.s.lengthOfLongestSubstringKDistinct(s, k))


if __name__ == "__main__":
    unittest.main()
