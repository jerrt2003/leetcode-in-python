import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "(()))"
        ans = 1
        self.assertEqual(ans, self.s.minInsertions(s))

    def test2(self):
        s = "())"
        ans = 0
        self.assertEqual(ans, self.s.minInsertions(s))

    def test3(self):
        s = "))())("
        ans = 3
        self.assertEqual(ans, self.s.minInsertions(s))


if __name__ == "__main__":
    unittest.main()
