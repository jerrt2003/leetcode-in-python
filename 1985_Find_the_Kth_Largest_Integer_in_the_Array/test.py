import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = ["3", "6", "7", "10"]
        k = 4
        ans = "3"

        self.assertEqual(ans, self.s.kthLargestNumber(nums, k))

    def test2(self):
        nums = ["2", "21", "12", "1"]
        k = 3
        ans = "2"

        self.assertEqual(ans, self.s.kthLargestNumber(nums, k))


if __name__ == "__main__":
    unittest.main()
