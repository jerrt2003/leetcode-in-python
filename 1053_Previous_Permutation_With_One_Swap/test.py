import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        arr = [3, 2, 1]
        ans = [3, 1, 2]
        self.assertEqual(ans, self.s.prevPermOpt1(arr))


if __name__ == "__main__":
    unittest.main()
