import unittest

from layoff import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1,2,3]
        out = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        self.assertEqual(self.s.permute(nums), out)

    def test2(self):
        nums = [1]
        out = [[1]]
        self.assertEqual(self.s.permute(nums), out)        


if __name__ == "__main__":
    unittest.main()