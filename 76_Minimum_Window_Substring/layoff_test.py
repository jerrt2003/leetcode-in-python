import unittest

from layoff import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    # def test1(self):
    #     s = "ADOBECODEBANC"
    #     t = "ABC"
    #     ans = "BANC"
    #     self.assertEqual(ans, self.s.minWindow(s, t))

    # def test2(self):
    #     s = "a"
    #     t = "a"
    #     ans = "a"
    #     self.assertEqual(ans, self.s.minWindow(s, t))

    # def test3(self):
    #     s = "a"
    #     t = "aa"
    #     ans = ""
    #     self.assertEqual(ans, self.s.minWindow(s, t))                        

    # def test4(self):
    #     s = "bba"
    #     t = "ab"
    #     ans = "ba"
    #     self.assertEqual(ans, self.s.minWindow(s, t))

    def test5(self):
        s = "aaaaaaaaaaaabbbbbcdd"
        t = "abcdd"
        ans = "abbbbbcdd"
        self.assertEqual(ans, self.s.minWindow(s, t))                                    


if __name__ == "__main__":
    unittest.main()