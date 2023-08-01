import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        citations = [3, 0, 6, 1, 5]
        ans = 3
        self.assertEqual(ans, self.s.hIndex(citations))


if __name__ == "__main__":
    unittest.main()
