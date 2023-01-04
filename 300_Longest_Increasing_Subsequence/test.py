import unittest

from layoff import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [10,9,2,5,3,7,101,18]
        ans = 4
        self.assertEqual(self.s.lengthOfLIS(nums), 4)


if __name__ == "__main__":
    unittest.main()