import unittest

from layoff import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1,3,4,2,2]
        ans = 2
        self.assertEqual(ans, self.s.findDuplicate(nums))

if __name__ == "__main__":
    unittest.main()