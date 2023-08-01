import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "()"
        self.assertTrue(self.s.checkValidString(s))

    def test2(self):
        s = "(*)"
        self.assertTrue(self.s.checkValidString(s))

    def test3(self):
        s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
        self.assertTrue(self.s.checkValidString(s))

    def test4(self):
        s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
        self.assertFalse(self.s.checkValidString(s))


if __name__ == "__main__":
    unittest.main()
