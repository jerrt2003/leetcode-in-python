import unittest

from solution import Solution

class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(Solution().validPalindrome('aba'), True)
        self.assertEqual(Solution().validPalindrome('abca'), True)
        self.assertEqual(Solution().validPalindrome('abc'), False)
        self.assertEqual(Solution().validPalindrome('abca'), True)
        self.assertEqual(Solution().validPalindrome('abcda'), False)


if __name__ == '__main__':
    unittest.main()