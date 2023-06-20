import unittest

from solution import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        input = "(()"
        sol = Solution()
        self.assertEqual(sol.longestValidParentheses(input), 2)

    def test2(self):
        input = ")()())"
        sol = Solution()
        self.assertEqual(sol.longestValidParentheses(input), 4)

    def test3(self):
        input = ""
        sol = Solution()
        self.assertEqual(sol.longestValidParentheses(input), 0)

    def test4(self):
        input = "(()()("
        sol = Solution()
        self.assertEqual(sol.longestValidParentheses(input), 4)

if __name__ == '__main__':
    unittest.main()