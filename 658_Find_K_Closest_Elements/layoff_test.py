import unittest

from layoff import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        arr = [1,2,3,4,5]
        k = 4
        x = 3
        ans = [1,2,3,4]
        self.assertEqual(self.s.findClosestElements(arr, k, x), ans)


if __name__ == "__main__":
    unittest.main()