import unittest

from layoff import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        firstList = [[0,2],[5,10],[13,23],[24,25]]
        secondList = [[1,5],[8,12],[15,24],[25,26]]
        ans = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        self.assertEqual(ans, self.s.intervalIntersection(firstList, secondList))

if __name__ == "__main__":
    unittest.main()