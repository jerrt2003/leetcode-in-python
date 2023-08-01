import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        n = 12
        ans = 21
        self.assertEqual(ans, self.s.nextGreaterElement(n))

    def test2(self):
        n = 21
        ans = -1
        self.assertEqual(ans, self.s.nextGreaterElement(n))

    def test3(self):
        n = 123
        ans = 132
        self.assertEqual(ans, self.s.nextGreaterElement(n))

    def test4(self):
        n = 2147483486
        ans = -1
        self.assertEqual(ans, self.s.nextGreaterElement(n))

    def test5(self):
        n = 12443322
        ans = 13222344
        self.assertEqual(ans, self.s.nextGreaterElement(n))


if __name__ == "__main__":
    unittest.main()
