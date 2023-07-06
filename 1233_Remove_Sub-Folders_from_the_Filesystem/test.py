import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
        ans = ["/a", "/c/d", "/c/f"]
        self.assertEqual(ans, self.s.removeSubfolders(folder))


if __name__ == "__main__":
    unittest.main()
