import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        n = 3
        out = ["((()))","(()())","(())()","()(())","()()()"]
        self.assertEqual(self.s.generateParenthesis(n), out)

if __name__ == "__main__":
    unittest.main()