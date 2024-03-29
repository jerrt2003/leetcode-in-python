import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1, 1, 1, 1, 1]
        target = 3
        out = 5
        self.assertEqual(self.s.findTargetSumWays(nums, target), out)


if __name__ == "__main__":
    unittest.main()
