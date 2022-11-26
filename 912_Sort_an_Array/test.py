import unittest
from quick_sort import Solution as qs
from merge_srot import Solution as ms

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.quick_sort = qs()
        self.merge_sort = ms()
        return super().setUp()

    def test1(self):
        nums = [3,4,1,2]
        ans = [1,2,3,4]
        self.assertEqual(self.quick_sort.sortArray(nums), ans)
        self.assertEqual(self.merge_sort.sortArray(nums), ans)

if __name__ == "__main__":
    unittest.main()