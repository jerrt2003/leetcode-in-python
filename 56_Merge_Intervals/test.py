import unittest
from stack import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        input = [[1,3],[2,6],[8,10],[15,18]]
        ans = [[1,6],[8,10],[15,18]]
        self.assertEqual(self.s.merge(input), ans)

    def test2(self):
        input = []
        ans = []
        self.assertEqual(self.s.merge(input), ans)

    def test3(self):
        input = [[1,10],[2,3]]
        ans = [[1,10]]
        self.assertEqual(self.s.merge(input), ans)                        

if __name__ == "__main__":
    unittest.main()