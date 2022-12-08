import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [4,3,2,7,8,2,3,1]
        ans = [2,3]
        self.assertEqual(self.s.findDuplicates(nums), ans)

if __name__ == "__main__":
    unittest.main()