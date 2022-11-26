import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()


    def test1(self):
        nums = [-1,0,1,2,-1,-4]
        self.assertEqual(self.s.threeSum(nums), [[-1,-1,2],[-1,0,1]])

    def test2(self):
        nums = [0,1,1]
        self.assertEqual(self.s.threeSum(nums), [])

    def test3(self):
        nums = [0,0,0]
        self.assertEqual(self.s.threeSum(nums), [[0,0,0]])                


if __name__ == "__main__":
    unittest.main()