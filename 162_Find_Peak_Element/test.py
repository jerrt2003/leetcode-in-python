import unittest
from binary_search import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1,2,3,1]
        self.assertEqual(self.s.findPeakElement(nums), 2)

    def test2(self):
        nums = [1,2,1,3,5,6,4]
        self.assertEqual(self.s.findPeakElement(nums), 5)

    def test3(self):
        """_summary_
        """
        nums = [1]
        self.assertEqual(self.s.findPeakElement(nums), 0)        


if __name__ == "__main__":
    unittest.main()