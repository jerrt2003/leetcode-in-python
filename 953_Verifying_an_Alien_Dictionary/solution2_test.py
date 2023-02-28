import unittest

from solution2 import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()
    
    def test1(self):
        words = ["hello","leetcode"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        self.assertTrue(self.s.isAlienSorted(words, order))

    def test2(self):
        words = ["ubg","kwh"]
        order = "qcipyamwvdjtesbghlorufnkzx"
        self.assertTrue(self.s.isAlienSorted(words, order))        

if __name__ == "__main__":
    unittest.main()