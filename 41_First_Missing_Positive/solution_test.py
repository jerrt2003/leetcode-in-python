import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()
    
    def test1(self):
        nums = [1,2,0]
        ans = 3
        self.assertEqual(ans, self.s.firstMissingPositive(nums))

    def test2(self):
        nums = [3,4,-1,1]
        ans = 2
        self.assertEqual(ans, self.s.firstMissingPositive(nums))

    def test3(self):
        nums = [7,8,9,11,12]
        ans = 1
        self.assertEqual(ans, self.s.firstMissingPositive(nums))                

    def test4(self):
        nums = [2,1]
        ans = 3
        self.assertEqual(ans, self.s.firstMissingPositive(nums))                        


if __name__ == "__main__":
    unittest.main()