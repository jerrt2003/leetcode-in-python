import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()

    def test1(self):
        s = "3[a]2[bc]"
        ans = "aaabcbc"
        self.assertEqual(ans, self.sol.decodeString(s))


if __name__ == "__main__":
    unittest.main()
