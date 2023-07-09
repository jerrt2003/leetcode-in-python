import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
        ans = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        self.assertEqual(ans, self.s.pacificAtlantic(heights))

    def test2(self):
        heights = [[1]]
        ans = [[0, 0]]
        self.assertEqual(ans, self.s.pacificAtlantic(heights))


if __name__ == "__main__":
    unittest.main()
