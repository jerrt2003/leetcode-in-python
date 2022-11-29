import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
        start = [0, 4]
        destination = [4, 4]
        self.assertTrue(self.s.hasPath(maze, start, destination))

    def test2(self):
        maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
        start = [0, 4]
        destination = [3, 2]
        self.assertFalse(self.s.hasPath(maze, start, destination))

    def test3(self):
        maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
        start = [4, 3]
        destination = [0, 1]
        self.assertFalse(self.s.hasPath(maze, start, destination))                        


if __name__ == "__main__":
    unittest.main()