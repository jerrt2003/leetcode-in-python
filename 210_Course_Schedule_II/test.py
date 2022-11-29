import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        numCourses = 2
        prerequisites = [[0,1]]
        self.assertEqual(self.s.findOrder(numCourses, prerequisites), [1,0])

    def test2(self):
        numCourses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        self.assertEqual(self.s.findOrder(numCourses, prerequisites), [0,2,1,3])        


if __name__ == "__main__":
    unittest.main()