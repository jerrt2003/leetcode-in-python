import unittest

from layoff import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        preorder = [1,2,4,5,3,6,7]
        postorder = [4,5,2,6,7,3,1]
        root = self.s.constructFromPrePost(preorder, postorder)
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()