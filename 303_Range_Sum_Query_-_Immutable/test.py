import unittest

from solution import NumArray

class Test(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test1(self):
        nums = [-2, 0, 3, -5, 2, -1]
        num_arr = NumArray(nums)
        self.assertEqual(num_arr.sumRange(0, 2), 1)
        self.assertEqual(num_arr.sumRange(2, 5), -1)
        self.assertEqual(num_arr.sumRange(0, 5), -3)

    def test2(self):
        nums = [0,0,1]
        num_arr = NumArray(nums)
        self.assertEqual(num_arr.sumRange(0, 2), 1)
        self.assertEqual(num_arr.sumRange(0, 0), 0)
        self.assertEqual(num_arr.sumRange(1, 0), 0)

    def test3(self):
        nums = []
        num_arr = NumArray(nums)
        self.assertEqual(num_arr.sumRange(0, 2), 0)


if __name__ == "__main__":
    unittest.main()