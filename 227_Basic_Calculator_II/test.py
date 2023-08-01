import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "3+2*2"
        ans = 7
        self.assertEqual(ans, self.s.calculate(s))

    def test2(self):
        s = "14-3/2"
        ans = 13
        self.assertEqual(ans, self.s.calculate(s))


if __name__ == "__main__":
    unittest.main()
