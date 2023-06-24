from solution2 import Solution
import unittest


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        intervals = [[0, 30], [5, 10], [15, 20]]
        self.assertFalse(self.s.canAttendMeetings(intervals))


if __name__ == "__main__":
    unittest.main()
