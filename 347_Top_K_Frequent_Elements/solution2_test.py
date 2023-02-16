import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1,1,1,2,2,3]
        k = 2
        ans = [2,1]
        self.assertEqual(ans, self.s.topKFrequent(nums, k))

    def test2(self):
        nums = [4,1,-1,2,-1,2,3]
        k = 2
        ans = [-1,2]
        self.assertEqual(ans, self.s.topKFrequent(nums, k))        


if __name__ == "__main__":
    unittest.main()