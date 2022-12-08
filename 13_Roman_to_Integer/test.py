import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "MCMXCIV"
        ans = 1994
        self.assertEqual(self.s.romanToInt(s), ans)

    def test2(self):
        s = "LVIII"
        ans = 58
        self.assertEqual(self.s.romanToInt(s), ans)        


if __name__ == "__main__":
    unittest.main()