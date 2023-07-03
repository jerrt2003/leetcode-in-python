import unittest
from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        output = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        self.assertEqual(self.s.combinationSum2(candidates, target), output)

    def test2(self):
        candidates = [2, 5, 2, 1, 2]
        target = 5
        output = [[1, 2, 2], [5]]
        self.assertEqual(self.s.combinationSum2(candidates, target), output)

    def test3(self):
        candidates = [3, 1, 3, 5, 1, 1]
        target = 8
        output = [[1, 1, 1, 5], [1, 1, 3, 3], [3, 5]]
        self.assertEqual(self.s.combinationSum2(candidates, target), output)


if __name__ == "__main__":
    unittest.main()
