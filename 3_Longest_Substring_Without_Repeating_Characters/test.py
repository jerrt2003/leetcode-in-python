import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        test_str = "abcabcbb"
        ans = 3
        self.assertEqual(self.s.lengthOfLongestSubstring(test_str), ans)

    def test2(self):
        test_str = "bbb"
        ans = 1
        self.assertEqual(self.s.lengthOfLongestSubstring(test_str), ans)        

    def test3(self):
        test_str = "pwwkew"
        ans = 3
        self.assertEqual(self.s.lengthOfLongestSubstring(test_str), ans)                

if __name__ == "__main__":
    unittest.main()