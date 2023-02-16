import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()


    def test1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        ans = [["bat"],["nat","tan"],["ate","eat","tea"]]
        self.assertEqual(ans, self.s.groupAnagrams(strs))


if __name__ == "__main__":
    unittest.main()