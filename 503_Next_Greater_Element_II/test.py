import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [1, 2, 1]
        ans = [2, -1, 2]
        self.assertEqual(ans, self.s.nextGreaterElements(nums))

    def test2(self):
        nums = [1, 2, 3, 4, 3]
        ans = [2, 3, 4, -1, 4]
        self.assertEqual(ans, self.s.nextGreaterElements(nums))

    def test3(self):
        nums = [1, 2, 3, 4, 5]
        ans = [2, 3, 4, 5, -1]
        self.assertEqual(ans, self.s.nextGreaterElements(nums))

    def test4(self):
        nums = [3, 2, 1]
        ans = [-1, 3, 3]
        self.assertEqual(ans, self.s.nextGreaterElements(nums))

    def test5(self):
        nums = [1]
        ans = [-1]
        self.assertEqual(ans, self.s.nextGreaterElements(nums))


if __name__ == "__main__":
    unittest.main()
