import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        n = 4
        edges = [[1, 0], [1, 2], [1, 3]]
        ans = [1]

        self.assertEqual(ans, self.s.findMinHeightTrees(n, edges))

    def test2(self):
        n = 6
        edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
        ans = [3, 4]

        self.assertEqual(ans, self.s.findMinHeightTrees(n, edges))

    def test3(self):
        n = 1
        edges = []
        ans = [0]

        self.assertEqual(ans, self.s.findMinHeightTrees(n, edges))

    def test4(self):
        n = 7
        edges = [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
        ans = [1, 2]

        self.assertEqual(ans, self.s.findMinHeightTrees(n, edges))


if __name__ == "__main__":
    unittest.main()
