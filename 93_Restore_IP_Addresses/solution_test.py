import unittest

from solution2 import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        s = "1234"
        ans = ["1.2.3.4"]
        self.assertEqual(ans, self.s.restoreIpAddresses(s))

    def test2(self):
        s = "25525511135"
        ans = ["255.255.11.135", "255.255.111.35"]
        self.assertEqual(ans, self.s.restoreIpAddresses(s))

    def test3(self):
        s = "0000"
        ans = ["0.0.0.0"]
        self.assertEqual(ans, self.s.restoreIpAddresses(s))

    def test4(self):
        s = "101023"
        ans = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
        self.assertEqual(ans, self.s.restoreIpAddresses(s))


if __name__ == "__main__":
    unittest.main()
