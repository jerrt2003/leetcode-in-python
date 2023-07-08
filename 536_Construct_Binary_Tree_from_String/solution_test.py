import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "1(2(3))"
        self.s.str2tree(s)

    def test2(self):
        s = "4"
        self.s.str2tree(s)


if __name__ == "__main__":
    unittest.main()
