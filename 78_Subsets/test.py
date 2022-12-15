import unittest

from layoff import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1,2,3]
        out = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        self.assertEqual(self.s.subsets(nums), out)

if __name__ == "__main__":
    unittest.main()