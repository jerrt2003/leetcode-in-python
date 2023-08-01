import unittest

from solution import Solution


class Test1(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        encoded1 = [[1, 3], [2, 3]]
        encoded2 = [[6, 3], [3, 3]]
        ans = [[6, 6]]

        self.assertEqual(ans, self.s.findRLEArray(encoded1, encoded2))

    def test2(self):
        encoded1 = [[1, 3], [2, 1], [3, 2]]
        encoded2 = [[2, 3], [3, 3]]
        ans = [[2, 3], [6, 1], [9, 2]]

        self.assertEqual(ans, self.s.findRLEArray(encoded1, encoded2))

    def test3(self):
        encoded1 = [[1, 1], [2, 1], [1, 1], [2, 1], [1, 1]]
        encoded2 = [[1, 1], [2, 1], [1, 1], [2, 1], [1, 1]]
        ans = [[1, 1], [4, 1], [1, 1], [4, 1], [1, 1]]

        self.assertEqual(ans, self.s.findRLEArray(encoded1, encoded2))


if __name__ == "__main__":
    unittest.main()
