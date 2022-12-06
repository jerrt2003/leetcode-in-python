import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [4,6,7,7]
        out = [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
        self.assertEqual(self.s.findSubsequences(nums), out)

if __name__ == "__main__":
    unittest.main()