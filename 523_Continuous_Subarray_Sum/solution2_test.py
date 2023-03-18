import unittest

from solution2 import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()
    
    def test1(self):
        nums = [23,2,4,6,7]
        k = 6
        self.assertTrue(self.s.checkSubarraySum(nums, k))

if __name__ == "__main__":
    unittest.main()