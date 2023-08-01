import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [2, -1, 2]
        k = 3
        ans = 3

        self.assertEqual(ans, self.s.shortestSubarray(nums, k))

    def test2(self):
        nums = [1]
        k = 1
        ans = 1

        self.assertEqual(ans, self.s.shortestSubarray(nums, k))

    def test3(self):
        nums = [1, 2]
        k = 4
        ans = -1

        self.assertEqual(ans, self.s.shortestSubarray(nums, k))

    def test4(self):
        nums = [84, -37, 32, 40, 95]
        k = 167
        ans = 3

        self.assertEqual(ans, self.s.shortestSubarray(nums, k))


if __name__ == "__main__":
    unittest.main()
