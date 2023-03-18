import unittest

from solution import Solution

class TestSolution(unittest.TestCase):
    def test_solution(self):
        nums = [3,2,1]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, [1,2,3])

        nums = [1,1]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, [1,1])        


if __name__ == '__main__':
    unittest.main()
