import unittest
from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [4,5,6,7,0,1,2]
        target = 0
        self.assertEqual(self.s.search(nums, target), 4)

    def test2(self):
        nums = [1,2,3,4,5,6]
        target = 1
        self.assertEqual(self.s.search(nums, target), 0)

    def test3(self):
        nums = [4,5,6,7,0,1,2]
        target = 8
        self.assertEqual(self.s.search(nums, target), -1)

    def test4(self):
        nums = [6,1,2,3,4,5]
        target = 5
        self.assertEqual(self.s.search(nums, target), 5)

    def test5(self):
        nums = []
        target = 1
        self.assertEqual(self.s.search(nums, target), -1)

    def test6(self):
        nums = [3,1]
        target = 3
        self.assertEqual(self.s.search(nums, target), 0)

    def test7(self):
        nums = [1]
        target = 0
        self.assertEqual(self.s.search(nums, target), -1)                

if __name__ == "__main__":
    unittest.main()