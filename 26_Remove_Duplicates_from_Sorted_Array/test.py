import unittest
from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1,1,2]
        ans = 2
        self.assertEqual(self.s.removeDuplicates(nums), ans)

    def test2(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        ans = 5
        self.assertEqual(self.s.removeDuplicates(nums), ans)        

if __name__ == "__main__":
    unittest.main()