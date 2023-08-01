import unittest

from solution import Solution
from solution2 import Solution as Solution2


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution2()
        return super().setUp()

    def test1(self):
        croakOfFrogs = "croakcroak"
        ans = 1
        self.assertEqual(ans, self.s.minNumberOfFrogs(croakOfFrogs))

    def test2(self):
        croakOfFrogs = "crcoakroak"
        ans = 2
        self.assertEqual(ans, self.s.minNumberOfFrogs(croakOfFrogs))

    def test3(self):
        croakOfFrogs = "croakcrook"
        ans = -1
        self.assertEqual(ans, self.s.minNumberOfFrogs(croakOfFrogs))

    def test4(self):
        croakOfFrogs = "ccccrrrrooooaaaakkkk"
        ans = 4
        self.assertEqual(ans, self.s.minNumberOfFrogs(croakOfFrogs))

    def test5(self):
        croakOfFrogs = "ccccrrrrooooaoaakkkk"
        ans = -1
        self.assertEqual(ans, self.s.minNumberOfFrogs(croakOfFrogs))

    def test6(self):
        croakOfFrogs = "aoocrrackk"
        ans = -1
        self.assertEqual(ans, self.s.minNumberOfFrogs(croakOfFrogs))

    def test7(self):
        croakOfFrogs = "croakroak"
        ans = -1
        self.assertEqual(ans, self.s.minNumberOfFrogs(croakOfFrogs))


if __name__ == "__main__":
    unittest.main()
