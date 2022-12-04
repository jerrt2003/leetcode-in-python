import unittest
from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        candidates = [10,1,2,7,6,1,5]
        target = 8
        output = [[1,1,6],[1,2,5],[1,7],[2,6]]
        self.assertEqual(self.s.combinationSum2(candidates, target), output)


if __name__ == "__main__":
    unittest.main()