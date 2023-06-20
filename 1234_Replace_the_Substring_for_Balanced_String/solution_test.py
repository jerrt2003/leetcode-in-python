import unittest

from solution2 import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()
    
    def test1(self):
        s = "QQQW"
        ans = 2
        self.assertEqual(ans, self.s.balancedString(s))

    def test2(self):
        s = "QQWE"
        ans = 1
        self.assertEqual(ans, self.s.balancedString(s))        




if __name__ == "__main__":
    unittest.main()