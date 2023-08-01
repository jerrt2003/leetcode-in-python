import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
        ans = [0, 2, 3, 1]
        self.assertEqual(ans, self.s.getOrder(tasks))

    def test2(self):
        tasks = [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]
        ans = [4, 3, 2, 0, 1]
        self.assertEqual(ans, self.s.getOrder(tasks))


if __name__ == "__main__":
    unittest.main()
