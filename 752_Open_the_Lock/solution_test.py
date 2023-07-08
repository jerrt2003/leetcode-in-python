import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        deadends = ["0201", "0101", "0102", "1212", "2002"]
        target = "0202"
        ans = 6

        self.assertEqual(ans, self.s.openLock(deadends, target))

    def test2(self):
        deadends = ["8888"]
        target = "0009"
        ans = 1

        self.assertEqual(ans, self.s.openLock(deadends, target))

    def test3(self):
        deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
        target = "8888"
        ans = -1

        self.assertEqual(ans, self.s.openLock(deadends, target))

    def test4(self):
        deadends = ["0000"]
        target = "8888"
        ans = -1

        self.assertEqual(ans, self.s.openLock(deadends, target))


if __name__ == "__main__":
    unittest.main()
