import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1,-1,5,-2,3]
        k = 3
        ans = 4
        self.assertEqual(ans, self.s.maxSubArrayLen(nums, k))

    def test2(self):
        nums = [-2,-1,2,1]
        k = 1
        ans = 2
        self.assertEqual(ans, self.s.maxSubArrayLen(nums, k))        

if __name__ == "__main__":
    unittest.main()