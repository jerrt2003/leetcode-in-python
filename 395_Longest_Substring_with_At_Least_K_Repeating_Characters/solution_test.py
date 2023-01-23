import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    # def test1(self):
    #     s = "aaabb"
    #     k = 3
    #     ans = 3
    #     self.assertEqual(ans, self.s.longestSubstring(s, k))

    def test2(self):
        s = "bbaaacbd"
        k = 3
        ans = 3
        self.assertEqual(ans, self.s.longestSubstring(s, k))

if __name__ == "__main__":
    unittest.main()