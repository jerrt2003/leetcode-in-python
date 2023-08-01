import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        n = 10
        ans = 4

        self.assertEqual(ans, self.s.rotatedDigits(n))

    def test2(self):
        n = 15
        ans = 6

        self.assertEqual(ans, self.s.rotatedDigits(n))

    def test3(self):
        n = 857
        ans = 247

        self.assertEqual(ans, self.s.rotatedDigits(n))


if __name__ == "__main__":
    unittest.main()
