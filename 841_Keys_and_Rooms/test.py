import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        rooms = [[1],[2],[3],[]]
        self.assertTrue(self.s.canVisitAllRooms(rooms))

    def test2(self):
        rooms = [[1,3],[3,0,1],[2],[0]]
        self.assertFalse(self.s.canVisitAllRooms(rooms))


if __name__ == "__main__":
    unittest.main()