import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        n = 12
        out = [[2,6],[3,4],[2,2,3]]
        self.assertEqual(self.s.getFactors(n), out)

    def test2(self):
        n = 1
        out = []
        self.assertEqual(self.s.getFactors(n), out)        

if __name__ == "__main__":
    unittest.main()