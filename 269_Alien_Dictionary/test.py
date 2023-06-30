import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        words = ["wrt", "wrf", "er", "ett", "rftt"]
        out = "wertf"
        self.assertEqual(self.s.alienOrder(words), out)

    def test2(self):
        words = ["z", "x"]
        out = "zx"
        self.assertEqual(self.s.alienOrder(words), out)

    def test3(self):
        words = ["z", "x", "z"]
        out = ""
        self.assertEqual(self.s.alienOrder(words), out)

    def test4(self):
        words = ["z", "z"]
        out = "z"
        self.assertEqual(self.s.alienOrder(words), out)

    # 測試 invalid input
    def test5(self):
        words = ["abc", "ab"]
        out = ""
        self.assertEqual(self.s.alienOrder(words), out)

    # 測試 invalid input (no valid topo sort found)
    def test6(self):
        words = ["z", "x", "a", "zb", "zx"]
        out = ""
        self.assertEqual(self.s.alienOrder(words), out)


if __name__ == "__main__":
    unittest.main()
