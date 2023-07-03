import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        maze = [
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0],
        ]
        start = [0, 4]
        dest = [4, 4]
        self.assertEqual(self.s.shortestDistance(maze, start, dest), 12)


if __name__ == "__main__":
    unittest.main()
