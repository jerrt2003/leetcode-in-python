import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [2,1,4,7,3,2,5]
        ans = 5
        self.assertEqual(ans, self.s.longestMountain(nums))

    def test2(self):
        nums = [2,2,2]
        ans = 0
        self.assertEqual(ans, self.s.longestMountain(nums))        

if __name__ == "__main__":
    unittest.main()