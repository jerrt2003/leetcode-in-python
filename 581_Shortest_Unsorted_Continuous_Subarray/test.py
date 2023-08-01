import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [2, 6, 4, 8, 10, 9, 15]
        self.assertEqual(5, self.s.findUnsortedSubarray(nums))


if __name__ == "__main__":
    unittest.main()
