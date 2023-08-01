import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        num = 2736
        ans = 7236
        self.assertEqual(ans, self.s.maximumSwap(num))

    def test2(self):
        num = 115
        ans = 511
        self.assertEqual(ans, self.s.maximumSwap(num))

    def test3(self):
        num = 19931227
        ans = 99131227
        self.assertEqual(ans, self.s.maximumSwap(num))


if __name__ == "__main__":
    unittest.main()
