import unittest

from layoff import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        heights = [2,1,5,6,2,3]
        ans = 10
        self.assertEqual(self.s.largestRectangleArea(heights), ans)


if __name__ == "__main__":
    unittest.main()