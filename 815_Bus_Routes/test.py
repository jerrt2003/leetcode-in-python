import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        routes = [[1, 2, 7], [3, 6, 7]]
        source = 1
        target = 6
        self.assertEqual(self.s.numBusesToDestination(routes, source, target), 2)

    def test2(self):
        routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
        source = 15
        target = 12
        self.assertEqual(self.s.numBusesToDestination(routes, source, target), -1)


if __name__ == "__main__":
    unittest.main()
