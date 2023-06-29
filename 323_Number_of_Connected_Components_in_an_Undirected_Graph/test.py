import unittest

from union_find import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        n = 5
        edges = [[0, 1], [1, 2], [3, 4]]
        ans = 2
        self.assertEqual(ans, self.s.countComponents(n, edges))

    def test2(self):
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        ans = 1
        self.assertEqual(ans, self.s.countComponents(n, edges))

    def test3(self):
        n = 1
        edges = []
        ans = 1
        self.assertEqual(ans, self.s.countComponents(n, edges))


if __name__ == "__main__":
    unittest.main()
