import unittest

from solution2 import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()
    
    def test1(self):
        nums = [1,3,5,4,7]
        ans = 3
        self.assertEqual(ans, self.s.findLengthOfLCIS(nums))

if __name__ == "__main__":
    unittest.main()