import unittest
from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1,2,5,9]
        threshold = 6
        self.assertEqual(self.s.smallestDivisor(nums, threshold), 5)

    def test2(self):
        nums = [44,22,33,11,1]
        threshold = 5
        self.assertEqual(self.s.smallestDivisor(nums, threshold), 44)

    def test3(self):
        nums = [1]
        threshold = 5
        self.assertEqual(self.s.smallestDivisor(nums, threshold), 1)

    def test4(self):
        nums = [21212,10101,12121]
        threshold = 1000000
        self.assertEqual(self.s.smallestDivisor(nums, threshold), 1)                        

if __name__ == "__main__":
    unittest.main()