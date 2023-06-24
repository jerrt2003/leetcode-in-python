from soltuon2 import Solution
import unittest

class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        num1 = "11"
        num2 = "123"
        ans = "134"
        self.assertEqual(ans, self.s.addStrings(num1, num2))


if __name__ == "__main__":
    unittest.main()