# -*- coding: utf-8 -*-
import bisect
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        Solution: DP
        Time Complexity: O(m*n*nlog(n))
        Space Complexity: O(n)
        Inspired By:
        - https://www.youtube.com/watch?v=yCQN096CwWM
        - https://www.quora.com/Given-an-array-of-integers-A-and-an-integer-k-find-a-subarray-that-contains-the-largest-sum-subject-to-a-constraint-that-the-sum-is-less-than-k
        - https://docs.python.org/2/library/bisect.html
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return 0
        def findMaxSumWithCap(array):
            _MAX = -float('inf')
            cumulative_res = [0]
            total = 0
            for elem in array:
                total += elem
                i = bisect.bisect_left(cumulative_res, total - k)
                if i != len(cumulative_res):
                    _MAX = max(_MAX, total - cumulative_res[i])
                bisect.insort(cumulative_res, total)
            return _MAX

        MAX = -float('inf')
        len_row = len(matrix)
        len_col = len(matrix[0])
        for i in range(len_row):
            sum_row = [0 for _ in range(len_col)]
            for j in range(i, len_row):
                sum_row = [x + y for x, y in zip(sum_row, matrix[j])]
                MAX = max(MAX, findMaxSumWithCap(sum_row))
        return MAX

matrix = [[1,0,1],[0,-2,3]]
k = 2

print Solution().maxSumSubmatrix(matrix, k)