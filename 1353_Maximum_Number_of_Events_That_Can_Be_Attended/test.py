import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        events = [[1, 2], [2, 3], [3, 4]]
        ans = 3

        self.assertEqual(ans, self.s.maxEvents(events))

    def test2(self):
        events = [[1, 2], [2, 3], [3, 4], [1, 2]]
        ans = 4

        self.assertEqual(ans, self.s.maxEvents(events))

    def test3(self):
        events = [
            [1, 1],
            [26, 27],
            [17, 17],
            [1, 2],
            [4, 7],
            [16, 16],
            [20, 23],
            [8, 9],
            [17, 19],
            [4, 4],
            [15, 15],
            [23, 27],
            [28, 31],
            [25, 26],
            [25, 29],
            [30, 33],
        ]
        ans = 16

        self.assertEqual(ans, self.s.maxEvents(events))

    def test4(self):
        events = [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]
        ans = 4

        self.assertEqual(ans, self.s.maxEvents(events))


if __name__ == "__main__":
    unittest.main()
