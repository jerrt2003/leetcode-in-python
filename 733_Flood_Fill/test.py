import unittest
from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr = 1
        sc = 1
        color = 2
        out = [[2,2,2],[2,2,0],[2,0,1]]
        self.assertEqual(self.s.floodFill(image, sr, sc, color), out)

    def test2(self):
        image = [[0,0,0],[0,0,0]]
        sr = 0
        sc = 0
        color = 0
        out = [[0,0,0],[0,0,0]]
        self.assertEqual(self.s.floodFill(image, sr, sc, color), out)        


if __name__ == "__main__":
    unittest.main()