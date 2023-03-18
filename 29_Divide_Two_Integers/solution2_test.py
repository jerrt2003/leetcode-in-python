import unittest

from solution2 import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()
    
    def test1(self):
        a = 10
        b = 3
        ans = 3
        self.assertEqual(ans, self.s.divide(10, 3))

if __name__ == "__main__":
    unittest.main()