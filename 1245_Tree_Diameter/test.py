import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        edges = [[0, 1], [0, 2]]
        ans = 2
        self.assertEqual(ans, self.s.treeDiameter(edges))

    def test2(self):
        edges = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]
        ans = 4
        self.assertEqual(ans, self.s.treeDiameter(edges))

    def test3(self):
        edges = [[0, 1]]
        ans = 1
        self.assertEqual(ans, self.s.treeDiameter(edges))


if __name__ == "__main__":
    unittest.main()
