import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [10, 5, 2, 6]
        k = 100
        ans = 8
        self.assertEqual(ans, self.s.numSubarrayProductLessThanK(nums, k))


if __name__ == "__main__":
    unittest.main()
