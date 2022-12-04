import unittest

from layoff import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        digits = "23"
        out = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertEqual(self.s.letterCombinations(digits), out)

    def test2(self):
        digits = "2"
        out = ["a","b","c"]
        self.assertEqual(self.s.letterCombinations(digits), out)        

if __name__ == "__main__":
    unittest.main()