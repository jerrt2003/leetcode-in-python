import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        arr = [3,9,8,6,4]
        ans = 1
        self.assertEqual(ans, self.s.peakIndexInMountainArray(arr))

if __name__ == "__main__":
    unittest.main()
    
