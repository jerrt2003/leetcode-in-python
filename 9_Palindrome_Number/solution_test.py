import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        num = 121
        self.assertTrue(self.s.isPalindrome(num))


if __name__ == "__main__":
    unittest.main()