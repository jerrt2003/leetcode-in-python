import unittest
from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1,2,2]
        out = [[],[1],[1,2],[1,2,2],[2],[2,2]]
        self.assertEqual(self.s.subsetsWithDup(nums), out)

if __name__ == "__main__":
    unittest.main()