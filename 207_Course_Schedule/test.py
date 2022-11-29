import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        numCourses = 2
        prerequisites = [[1,0]]
        self.assertTrue(self.s.canFinish(numCourses, prerequisites))

    def test2(self):
        numCourses = 2
        prerequisites = [[1,0],[0,1]]
        self.assertFalse(self.s.canFinish(numCourses, prerequisites))        


if __name__ == "__main__":
    unittest.main()