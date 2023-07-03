import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "aab"
        ans = [["a", "a", "b"], ["aa", "b"]]
        self.assertEqual(ans, self.s.partition(s))


if __name__ == "__main__":
    unittest.main()
