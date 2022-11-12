# -*- coding: utf-8 -*-
class Solution(object):
    def combine(self, n, k):
        """
        Solution: backtracking
        Time Complexity: O(n!)
        Space Complexity:
        Perf: Runtime: 192 ms, faster than 72.41% / Memory Usage: 13.2 MB, less than 5.36％
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def helper(curr_comb, start, end, res, k):
            if end - start+1 + 1 < k: # !! 若剩下的數不夠K的話不需在往下走
                return
            if k == 0:
                res.append(curr_comb)
                return
            for i in range(start, end):
                helper(curr_comb + [i], i+1, end, res, k-1)
        res = []
        helper([], 1, n+1, res, k)
        return res

print Solution().combine(4, 2)