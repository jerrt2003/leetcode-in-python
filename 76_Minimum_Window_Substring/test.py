from solution import Solution
import unittest


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        ans = "BANC"
        self.assertEqual(ans, self.s.minWindow(s, t))

    def test2(self):
        s = "a"
        t = "a"
        ans = "a"
        self.assertEqual(ans, self.s.minWindow(s, t))


if __name__ == "__main__":
    unittest.main()
