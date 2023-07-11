import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        edges = [[1, 2], [1, 3], [2, 3]]
        ans = [2, 3]
        self.assertEqual(ans, self.s.findRedundantConnection(edges))


if __name__ == "__main__":
    unittest.main()
