import unittest
from solution import MedianFinder

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.finder = MedianFinder()
        return super().setUp()

    def test1(self): 
        self.finder.addNum(1)
        self.finder.addNum(2)
        self.finder.addNum(3)
        self.assertEqual(self.finder.findMedian(), 2)

    def test2(self): 
        self.finder.addNum(-1)
        self.finder.addNum(-2)
        self.finder.addNum(-3)
        self.finder.addNum(-4)
        self.assertEqual(self.finder.findMedian(), -2.5)        

if __name__ == "__main__":
    unittest.main()