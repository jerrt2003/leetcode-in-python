# -*- coding: utf-8 -*-
class Solution(object):
    def combine(self, n, k):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!! (588ms, beat 49.1%)
        TP:
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def doComb(comb, i):
            if len(comb) == k:
                res.append(comb)
                return
            for i in range(i, n+1):
                doComb(comb + [i], i + 1)
        doComb([], 1)
        return res

n = 5
k = 3

print Solution().combine(n, k)