import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        grid = [[5, 4, 5], [1, 2, 6], [7, 4, 6]]
        ans = 4
        self.assertEqual(ans, self.s.maximumMinimumPath(grid))


if __name__ == "__main__":
    unittest.main()
