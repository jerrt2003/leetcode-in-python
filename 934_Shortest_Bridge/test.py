import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        grid = [[0, 1], [1, 0]]
        ans = 1

        self.assertEqual(ans, self.s.shortestBridge(grid))

    def test2(self):
        grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
        ans = 2

        self.assertEqual(ans, self.s.shortestBridge(grid))

    def test3(self):
        grid = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]
        ans = 1

        self.assertEqual(ans, self.s.shortestBridge(grid))


if __name__ == "__main__":
    unittest.main()
