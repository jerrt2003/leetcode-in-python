import unittest

from solution3 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        lo = 12
        hi = 15
        k = 2
        ans = 13
        self.assertEqual(ans, self.s.getKth(lo, hi, k))

    def test2(self):
        lo = 7
        hi = 11
        k = 4
        ans = 7
        self.assertEqual(ans, self.s.getKth(lo, hi, k))

    def test3(self):
        lo = 1
        hi = 1000
        k = 777
        ans = 570
        self.assertEqual(ans, self.s.getKth(lo, hi, k))


if __name__ == "__main__":
    unittest.main()
