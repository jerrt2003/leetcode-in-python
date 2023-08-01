import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        word = "internationalization"
        abbr = "i12iz4n"

        self.assertTrue(self.s.validWordAbbreviation(word, abbr))

    def test2(self):
        word = "apple"
        abbr = "a2e"

        self.assertFalse(self.s.validWordAbbreviation(word, abbr))

    def test3(self):
        word = "substitution"
        abbr = "12"

        self.assertTrue(self.s.validWordAbbreviation(word, abbr))

    def test4(self):
        word = "substitution"
        abbr = "s55n"

        self.assertFalse(self.s.validWordAbbreviation(word, abbr))

    def test5(self):
        word = "substitution"
        abbr = "s010n"

        self.assertFalse(self.s.validWordAbbreviation(word, abbr))

    def test6(self):
        word = "substitution"
        abbr = "s0ubstitution"

        self.assertFalse(self.s.validWordAbbreviation(word, abbr))


if __name__ == "__main__":
    unittest.main()
