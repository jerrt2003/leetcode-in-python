import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        n = 3
        restrictions = [[0, 1]]
        requests = [[0, 2], [2, 1]]
        ans = [True, False]

        self.assertEqual(ans, self.s.friendRequests(n, restrictions, requests))

    def test2(self):
        n = 3
        restrictions = [[0, 1]]
        requests = [[1, 2], [0, 2]]
        ans = [True, False]

        self.assertEqual(ans, self.s.friendRequests(n, restrictions, requests))

    def test3(self):
        n = 5
        restrictions = [[0, 1], [1, 2], [2, 3]]
        requests = [[0, 4], [1, 2], [3, 1], [3, 4]]
        ans = [True, False, True, False]

        self.assertEqual(ans, self.s.friendRequests(n, restrictions, requests))


if __name__ == "__main__":
    unittest.main()
