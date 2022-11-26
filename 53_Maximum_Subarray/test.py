import unittest
from dp import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1,2,3,4]
        ans = 10
        self.assertEqual(self.s.maxSubArray(nums), ans)

    def test2(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        ans = 6
        self.assertEqual(self.s.maxSubArray(nums), ans)

    def test3(self):
        nums = [0,0,-1]
        ans = 0
        self.assertEqual(self.s.maxSubArray(nums), ans)

    def test4(self):
        nums = [1,0,1,0]
        ans = 2
        self.assertEqual(self.s.maxSubArray(nums), ans)                

    def test5(self):
        nums = []
        ans = 0
        self.assertEqual(self.s.maxSubArray(nums), ans)

    def test6(self):
        nums = [5,4,-1,7,8]
        ans = 23
        self.assertEqual(self.s.maxSubArray(nums), ans)                        

if __name__ == "__main__":
    unittest.main()