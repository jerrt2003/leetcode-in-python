import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [3,2,1,5,6,4]
        k = 2
        ans = 5
        self.assertEqual(5, self.s.findKthLargest(nums, k))

if __name__ == "__main__":
    unittest.main()