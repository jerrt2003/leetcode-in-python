import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        graph = [[1, 2], [3], [3], []]
        ans = [[0, 1, 3], [0, 2, 3]]
        self.assertEqual(ans, self.s.allPathsSourceTarget(graph))

    def test2(self):
        graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
        ans = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
        self.assertEqual(ans, self.s.allPathsSourceTarget(graph))


if __name__ == "__main__":
    unittest.main()
