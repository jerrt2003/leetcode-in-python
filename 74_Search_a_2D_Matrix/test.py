import unittest
from solution3 import Solution


class Test(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        """_summary_"""
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 60
        self.assertTrue(self.s.searchMatrix(matrix, target))

    def test2(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        self.assertFalse(self.s.searchMatrix(matrix, target))

    def test3(self):
        matrix = [[1]]
        target = 1
        self.assertTrue(self.s.searchMatrix(matrix, target))

    def test4(self):
        matrix = [[1]]
        target = 2
        self.assertFalse(self.s.searchMatrix(matrix, target))

    def test5(self):
        """_summary_"""
        matrix = [[]]
        target = 2
        self.assertFalse(self.s.searchMatrix(matrix, target))


if __name__ == "__main__":
    unittest.main()
