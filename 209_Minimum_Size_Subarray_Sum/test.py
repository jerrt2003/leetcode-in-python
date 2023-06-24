import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        target = 7
        nums = [2, 3, 1, 2, 4, 3]
        ans = 2

        self.assertEqual(2, self.s.minSubArrayLen(target, nums))


if __name__ == "__main__":
    unittest.main()
