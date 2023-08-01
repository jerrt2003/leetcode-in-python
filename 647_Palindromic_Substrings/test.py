import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        self.assertEqual(self.s.countSubstrings("fdsklf"), 6)


if __name__ == "__main__":
    unittest.main()
