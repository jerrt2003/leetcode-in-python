import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()
    
    def test1(self):
        nums = [4,7,9,10]
        k = 1
        ans = 5
        self.assertEqual(ans, self.s.missingElement(nums, k))

    def test2(self):
        nums = [4,7,9,10]
        k = 3
        ans = 8
        self.assertEqual(ans, self.s.missingElement(nums, k))        


if __name__ == "__main__":
    unittest.main()