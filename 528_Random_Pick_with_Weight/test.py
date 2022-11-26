import unittest
from prefix_solution import Solution

class Test(unittest.TestCase):
    
    def test1(self):
        nums = [1]
        ans = 0
        self.s = Solution(nums)
        self.assertEqual(self.s.pickIndex(), ans)

    def test2(self):
        nums = [1, 3]
        self.s = Solution(nums)
        self.assertEqual(self.s.pickIndex(), 1)

if __name__ == "__main__":
    unittest.main()
