import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        ans = 1
        self.assertEqual(ans, self.s.eraseOverlapIntervals(intervals))

    def test2(self):
        intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
        ans = 2
        self.assertEqual(ans, self.s.eraseOverlapIntervals(intervals))

    def test3(self):
        intervals = [
            [-52, 31],
            [-73, -26],
            [82, 97],
            [-65, -11],
            [-62, -49],
            [95, 99],
            [58, 95],
            [-31, 49],
            [66, 98],
            [-63, 2],
            [30, 47],
            [-40, -26],
        ]
        ans = 7
        self.assertEqual(ans, self.s.eraseOverlapIntervals(intervals))


if __name__ == "__main__":
    unittest.main()
