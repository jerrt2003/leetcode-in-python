import unittest
from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1,1,1]
        k = 2
        self.assertEqual(self.s.subarraySum(nums, k), 2)

    def test2(self):
        nums = [1,2,3]
        k = 3
        self.assertEqual(self.s.subarraySum(nums, k), 2)

    def test3(self):
        nums = [3,2,1]
        k = 3
        self.assertEqual(self.s.subarraySum(nums, k), 2)

    def test4(self):
        nums = [0,0,0]
        k = 1
        self.assertEqual(self.s.subarraySum(nums, k), 0)

    def test5(self):
        nums = [1]
        k = 0
        self.assertEqual(self.s.subarraySum(nums, k), 0)        

if __name__ == "__main__":
    unittest.main()