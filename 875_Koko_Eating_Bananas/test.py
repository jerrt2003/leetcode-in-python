import unittest
from solution import Solution

class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test1(self):
        piles = [3,6,7,11]
        h = 8
        self.assertEqual(self.s.minEatingSpeed(piles, 8), 4)

if __name__ == '__main__':
    unittest.main()