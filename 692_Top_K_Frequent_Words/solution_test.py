import unittest

from solution import Solution

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        return super().setUp()

    def test1(self):
        words = ["i","love","leetcode","i","love","coding"]
        k = 2
        ans = ["i","love"]
        self.assertEqual(self.s.topKFrequent(words, k), ans)

    def test2(self):
        words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
        k = 4
        ans = ["the","is","sunny","day"]
        self.assertEqual(self.s.topKFrequent(words, k), ans)        


if __name__ == "__main__":
    unittest.main()