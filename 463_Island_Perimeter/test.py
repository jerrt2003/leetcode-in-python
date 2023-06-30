import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        ans = 16

        self.assertEqual(ans, self.s.islandPerimeter(grid))

    def test2(self):
        grid = [[1]]
        ans = 4

        self.assertEqual(ans, self.s.islandPerimeter(grid))

    def test3(self):
        grid = [[1, 0]]
        ans = 4

        self.assertEqual(ans, self.s.islandPerimeter(grid))


if __name__ == "__main__":
    unittest.main()
