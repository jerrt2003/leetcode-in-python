import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        k = 8
        ans = 13

        self.assertEqual(ans, self.s.kthSmallest(matrix, k))

    def test1(self):
        matrix = [[1, 8, 9], [8, 9, 9], [8, 9, 9]]
        k = 8
        ans = 13

        self.assertEqual(ans, self.s.kthSmallest(matrix, k))


if __name__ == "__main__":
    unittest.main()
