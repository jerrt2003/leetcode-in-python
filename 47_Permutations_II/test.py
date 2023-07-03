import unittest
from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1, 1, 2]
        out = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        self.assertEqual(self.s.permuteUnique(nums), out)

    def test2(self):
        nums = [3, 3, 0, 3]
        out = [[0, 3, 3, 3], [3, 0, 3, 3], [3, 3, 0, 3], [3, 3, 3, 0]]
        self.assertEqual(self.s.permuteUnique(nums), out)


if __name__ == "__main__":
    unittest.main()
