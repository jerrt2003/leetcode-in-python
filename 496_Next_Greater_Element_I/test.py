import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums1 = [4, 1, 2]
        nums2 = [1, 3, 4, 2]
        ans = [-1, 3, -1]

        self.assertEqual(ans, self.s.nextGreaterElement(nums1, nums2))

    def test2(self):
        nums1 = [2, 4]
        nums2 = [1, 2, 3, 4]
        ans = [3, -1]

        self.assertEqual(ans, self.s.nextGreaterElement(nums1, nums2))


if __name__ == "__main__":
    unittest.main()
