# -*- coding: utf-8 -*-
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        Solution: DP
        Time Complexity: O(n)
        Space Complexity: O(n)
        Perf: Runtime: 20 ms, faster than 90.41%  / Memory Usage: 10.8 MB, less than 92.11%
        Inspired By: https://leetcode.com/problems/arithmetic-slices/solution/
        :type A: List[int]
        :rtype: int
        """
        m = len(A)
        DP = [0 for _ in range(m)]
        sum = 0
        for i in range(2, m):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                DP[i] = DP[i-1] + 1
                sum += DP[i]
        return sum