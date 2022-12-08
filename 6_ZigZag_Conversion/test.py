import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "PAYPALISHIRING"
        num_rows = 3
        ans = "PAHNAPLSIIGYIR"
        self.assertEqual(self.s.convert(s, num_rows), ans)


if __name__ == "__main__":
    unittest.main()