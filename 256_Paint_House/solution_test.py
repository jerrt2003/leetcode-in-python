import unittest

# from solution import Solution
from dp import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        costs = [[17,2,17],[16,16,5],[14,3,19]]
        ans = 10
        self.assertEqual(ans, self.s.minCost(costs))

if __name__ == "__main__":
    unittest.main()