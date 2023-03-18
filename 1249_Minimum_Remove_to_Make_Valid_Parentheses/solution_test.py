import unittest

from solution2 import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "lee(t(c)o)de)"
        ans = "lee(t(c)o)de"
        self.assertEqual(ans, self.s.minRemoveToMakeValid(s))


if __name__ == "__main__":
    unittest.main()