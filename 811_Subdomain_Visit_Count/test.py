import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        cpdomains = ["9001 discuss.leetcode.com"]
        ans = ["9001 leetcode.com", "9001 discuss.leetcode.com", "9001 com"]
        self.assertEqual(ans, self.s.subdomainVisits(cpdomains))


if __name__ == "__main__":
    unittest.main()
