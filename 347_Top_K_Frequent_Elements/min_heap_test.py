import unittest

from min_heap import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1,1,1,2,2,3]
        k = 2
        ans = [1,2]
        self.assertEqual(ans, self.s.topKFrequent(nums, k))

if __name__ == "__main__":
    unittest.main()