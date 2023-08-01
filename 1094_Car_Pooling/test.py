import unittest

from solution import Solution


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        trips = [[2, 1, 5], [3, 3, 7]]
        capacity = 4
        self.assertFalse(self.s.carPooling(trips, capacity))

    def test2(self):
        trips = [[2, 1, 5], [3, 3, 7]]
        capacity = 5
        self.assertTrue(self.s.carPooling(trips, capacity))


if __name__ == "__main__":
    unittest.main()
