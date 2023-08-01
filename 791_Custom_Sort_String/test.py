import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test_customSortString(self):
        order = "cba"
        s = "abcd"
        self.assertEqual("dcba", self.s.customSortString(order, s))


if __name__ == "__main__":
    unittest.main()
