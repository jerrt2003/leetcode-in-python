import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        n = 4
        k = 2
        out = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        self.assertEqual(self.s.combine(n,k), out)

if __name__ == "__main__":
    unittest.main()