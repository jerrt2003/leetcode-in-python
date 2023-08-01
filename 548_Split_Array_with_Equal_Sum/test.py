import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1, 2, 1, 2, 1, 2, 1]
        self.assertTrue(self.s.splitArray(nums))


if __name__ == "__main__":
    unittest.main()
