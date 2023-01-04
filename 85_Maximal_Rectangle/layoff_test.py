import unittest

from layoff import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        ans = 6
        self.assertEqual(self.s.maximalRectangle(matrix), ans)

    def test2(self):
        matrix = [["1"]]
        ans = 1
        self.assertEqual(self.s.maximalRectangle(matrix), ans)        

    def test3(self):
        matrix = [["0"]]
        ans = 0
        self.assertEqual(self.s.maximalRectangle(matrix), ans)        

if __name__ == "__main__":
    unittest.main()