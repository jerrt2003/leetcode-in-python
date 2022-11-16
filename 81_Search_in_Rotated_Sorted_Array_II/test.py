import unittest
from solution2 import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [2,5,6,0,0,1,2]
        target = 0
        self.assertTrue(self.s.search(nums, target))

    def test2(self):
        nums = [4,5,6,3,3,3]
        target = 3
        self.assertTrue(self.s.search(nums, target))

    def test3(self):
        nums = [1,1,1,1,1]
        target = 2
        self.assertFalse(self.s.search(nums, target))

    def test4(self):
        nums = [4,1,2,3]
        target = 4
        self.assertTrue(self.s.search(nums, target))

    def test5(self):
        nums = [2,5,6,0,0,1,2]
        target = 3
        self.assertFalse(self.s.search(nums, target))

    def test6(self):
        nums = [3,1]
        target = 3
        self.assertTrue(self.s.search(nums, target))

    def test7(self):
        nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
        target = 2
        self.assertTrue(self.s.search(nums, target))

    def test8(self):
        nums = [2,2,2,0,2,2]
        target = 0
        self.assertTrue(self.s.search(nums, target))                


if __name__ == "__main__":
    unittest.main()