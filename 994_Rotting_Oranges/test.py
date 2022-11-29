import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        out = 4
        self.assertEqual(self.s.orangesRotting(grid), out)

    def test2(self):
        grid = [[0, 2]]
        out = 0
        self.assertEqual(self.s.orangesRotting(grid), out)        

if __name__ == "__main__":
    unittest.main()