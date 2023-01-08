import unittest

from monotone_stack import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        ans = 6
        self.assertEqual(ans, self.s.trap(height))

    def test2(self):
        height = [4,2,0,3,2,5]
        ans = 9
        self.assertEqual(ans, self.s.trap(height))        

if __name__ == "__main__":
    unittest.main()