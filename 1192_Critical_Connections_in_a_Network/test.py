import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        n = 4
        connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
        ans = [[1, 3]]

        self.assertEqual(ans, self.s.criticalConnections(n, connections))


if __name__ == "__main__":
    unittest.main()
