import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "bab"
        t = "aba"
        ans = 1

        self.assertEqual(ans, self.s.minSteps(s, t))

    def test2(self):
        s = "leetcode"
        t = "practice"
        ans = 5

        self.assertEqual(ans, self.s.minSteps(s, t))


if __name__ == "__main__":
    unittest.main()
