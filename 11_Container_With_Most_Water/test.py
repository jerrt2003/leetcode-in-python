import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        ans = 49
        self.assertEqual(ans, self.s.maxArea(height))

    def test2(self):
        height = [1, 1]
        ans = 1
        self.assertEqual(ans, self.s.maxArea(height))


if __name__ == "__main__":
    unittest.main()
