import unittest

from dp import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "babad"
        ans = "bab"

        self.assertEqual(ans, self.s.longestPalindrome(s))


if __name__ == "__main__":
    unittest.main()
