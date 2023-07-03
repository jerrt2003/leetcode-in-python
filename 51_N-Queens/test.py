import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        n = 4
        out = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
        self.assertEqual(self.s.solveNQueens(n), out)

    def test2(self):
        n = 1
        out = [["Q"]]
        self.assertEqual(self.s.solveNQueens(n), out)


if __name__ == "__main__":
    unittest.main()
