import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        mat = [[0,0,0],[0,1,0],[0,0,0]]
        out = [[0,0,0],[0,1,0],[0,0,0]]
        self.assertEqual(self.s.updateMatrix(mat), out)

    def test2(self):
        mat = [[0,0,0],[0,1,0],[1,1,1]]
        out = [[0,0,0],[0,1,0],[1,2,1]]
        self.assertEqual(self.s.updateMatrix(mat), out)        

if __name__ == "__main__":
    unittest.main()