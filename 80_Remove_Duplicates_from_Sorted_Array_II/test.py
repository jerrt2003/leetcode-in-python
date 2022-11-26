import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1,1,1,2,2,3]
        self.assertEqual(self.s.removeDuplicates(nums), 5)

if __name__ == "__main__":
    unittest.main()