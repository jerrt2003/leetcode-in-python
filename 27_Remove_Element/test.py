import unittest
from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        nums = [3, 2, 2, 3]
        remove = 3
        ans = 2
        self.assertEqual(self.s.removeElement(nums, remove), ans)

    def test2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        remove = 2
        ans = 5
        self.assertEqual(self.s.removeElement(nums, remove), ans)

    def test3(self):
        nums = [1, 1]
        remove = 1
        ans = 0
        self.assertEqual(self.s.removeElement(nums, remove), ans)

    def test4(self):
        nums = []
        remove = 1
        ans = 0
        self.assertEqual(self.s.removeElement(nums, remove), ans)


if __name__ == "__main__":
    unittest.main()
