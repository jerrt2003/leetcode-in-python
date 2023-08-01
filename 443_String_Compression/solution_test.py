import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        ans = 6
        self.assertEqual(ans, self.s.compress(chars))

    def test2(self):
        chars = ["a"]
        ans = 1
        self.assertEqual(ans, self.s.compress(chars))

    def test3(self):
        chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
        ans = 4
        self.assertEqual(ans, self.s.compress(chars))

    def test4(self):
        chars = ["a", "a", "a", "b", "b", "a", "a"]
        ans = 6
        self.assertEqual(ans, self.s.compress(chars))

    def test5(self):
        chars = ["b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c", "c"]
        ans = 5
        self.assertEqual(ans, self.s.compress(chars))


if __name__ == "__main__":
    unittest.main()
