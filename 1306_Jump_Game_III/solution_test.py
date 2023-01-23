import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        arr = [4,2,3,0,3,1,2]
        start = 5
        self.assertTrue(self.s.canReach(arr, start))

    def test2(self):
        arr = [4,2,3,0,3,1,2]
        start = 0
        self.assertTrue(self.s.canReach(arr, start))

    def test3(self):
        arr = [3,0,2,1,2]
        start = 2
        self.assertFalse(self.s.canReach(arr, start))                


if __name__ == "__main__":
    unittest.main()