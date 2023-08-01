import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        ans = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        self.assertEqual(ans, self.s.reconstructQueue(people))


if __name__ == "__main__":
    unittest.main()
