import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
        self.assertTrue(self.s.isBipartite(graph))

    def test2(self):
        graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
        self.assertFalse(self.s.isBipartite(graph))


if __name__ == "__main__":
    unittest.main()
