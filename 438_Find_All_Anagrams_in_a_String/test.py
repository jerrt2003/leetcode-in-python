from solution2 import Solution

import unittest


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "cbaebabacd"
        p = "abc"
        ans = [0, 6]
        self.assertEqual(ans, self.s.findAnagrams(s, p))


if __name__ == "__main__":
    unittest.main()
