import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [4, 3, 2, 3, 5, 2, 1]
        k = 4
        self.assertTrue(self.s.canPartitionKSubsets(nums, k))

    def test2(self):
        nums = [1, 2, 3, 4]
        k = 3
        self.assertFalse(self.s.canPartitionKSubsets(nums, k))

    def test3(self):
        nums = [1]
        k = 1
        self.assertTrue(self.s.canPartitionKSubsets(nums, k))

    def test4(self):
        nums = [
            3522,
            181,
            521,
            515,
            304,
            123,
            2512,
            312,
            922,
            407,
            146,
            1932,
            4037,
            2646,
            3871,
            269,
        ]
        k = 5
        self.assertTrue(self.s.canPartitionKSubsets(nums, k))

    def test5(self):
        nums = [85, 35, 40, 64, 86, 45, 63, 16, 5364, 110, 5653, 97, 95]
        k = 7
        self.assertTrue(self.s.canPartitionKSubsets(nums, k))


if __name__ == "__main__":
    unittest.main()
