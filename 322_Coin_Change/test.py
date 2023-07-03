import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        coins = [1, 2, 5]
        amount = 11
        ans = 3

        self.assertEqual(ans, self.s.coinChange(coins, amount))

    def test2(self):
        coins = [186, 419, 83, 408]
        amount = 6249
        ans = 20

        self.assertEqual(ans, self.s.coinChange(coins, amount))

    def test3(self):
        coins = [1, 2, 3]
        amount = 6
        ans = 2

        self.assertEqual(ans, self.s.coinChange(coins, amount))


if __name__ == "__main__":
    unittest.main()
