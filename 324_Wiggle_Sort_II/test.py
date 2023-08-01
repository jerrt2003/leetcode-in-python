import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1, 5, 1, 1, 6, 4]
        self.s.wiggleSort(nums)
        self.assertEqual(nums, [1, 6, 1, 5, 1, 4])

    def test2(self):
        nums = [1, 4, 3, 4, 1, 2, 1, 3, 1, 3, 2, 3, 3]
        self.s.wiggleSort(nums)
        self.assertEqual(nums, [3, 4, 2, 4, 2, 3, 1, 3, 1, 3, 1, 3, 1])


if __name__ == "__main__":
    unittest.main()
