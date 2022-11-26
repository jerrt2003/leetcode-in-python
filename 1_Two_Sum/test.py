import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [2,7,11,15]
        target = 9
        self.assertEqual(self.s.twoSum(nums, target), [0, 1])


if __name__ == "__main__":
    unittest.main()