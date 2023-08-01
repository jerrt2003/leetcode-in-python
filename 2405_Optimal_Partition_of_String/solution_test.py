import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "abacaba"
        ans = 4
        self.assertEqual(ans, self.s.partitionString(s))


if __name__ == "__main__":
    unittest.main()
