import unittest

from layoff import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3
        ans = [3,3,5,5,6,7]
        self.assertEqual(self.s.maxSlidingWindow(nums,k),ans)

    def test2(self):
        nums = [1]
        k = 1
        ans = [1]
        self.assertEqual(self.s.maxSlidingWindow(nums,k),ans)        

if __name__ == "__main__":
    unittest.main()