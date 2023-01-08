import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]]
        x = 0
        y = 2
        self.assertEqual(self.s.minArea(image, x, y), 6)

    def test2(self):
        image = [["1"]]
        x = 0
        y = 0
        self.assertEqual(self.s.minArea(image, x, y), 1)        



if __name__ == "__main__":
    unittest.main()