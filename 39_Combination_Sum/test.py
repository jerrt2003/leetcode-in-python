import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        candidates = [2,3,6,7]
        target = 7
        out = [[2,2,3],[7]]
        self.assertEqual(self.s.combinationSum(candidates, target), out)

    def test2(self):
        candidates = [2,3,5]
        target = 8
        out =  [[2,2,2,2],[2,3,3],[3,5]]
        self.assertEqual(self.s.combinationSum(candidates, target), out)

    def test3(self):
        candidates = [2]
        target = 1
        out =  []
        self.assertEqual(self.s.combinationSum(candidates, target), out)                


if __name__ == "__main__":
    unittest.main()