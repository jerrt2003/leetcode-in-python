import unittest

from layoff import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        intervals = [[0,30],[5,10],[15,20]]
        ans = 2
        self.assertEqual(ans, self.s.minMeetingRooms(intervals))

if __name__ == "__main__":
    unittest.main()