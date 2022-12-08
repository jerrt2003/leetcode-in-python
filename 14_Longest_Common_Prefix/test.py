import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        strs = ["flower","flow","flight"]
        ans = "fl"
        self.assertEqual(self.s.longestCommonPrefix(strs), ans)

    def test2(self):
        strs = ["dog","racecar","car"]
        ans = ""
        self.assertEqual(self.s.longestCommonPrefix(strs), ans)        


if __name__ == "__main__":
    unittest.main()