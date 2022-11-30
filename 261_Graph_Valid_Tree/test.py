import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        n = 5
        edges = [[0,1],[0,2],[0,3],[1,4]]
        self.assertTrue(self.s.validTree(n, edges))

    def test2(self):
        n = 5
        edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
        self.assertFalse(self.s.validTree(n, edges))

    def test3(self):
        n = 1
        edges = []
        self.assertTrue(self.s.validTree(n, edges))                        


if __name__ == "__main__":
    unittest.main()