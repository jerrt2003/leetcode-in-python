import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()
    
    def test1(self):
        num = "1432219"
        k = 3
        ans = "1219"

        self.assertEqual(ans, self.s.removeKdigits(num, k))

    def test2(self):
        num = "10200"
        k = 1
        ans = "200"

        self.assertEqual(ans, self.s.removeKdigits(num, k))        


if __name__ == "__main__":
    unittest.main()