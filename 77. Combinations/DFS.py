# -*- coding: utf-8 -*-
class Solution(object):
    def combine(self, n, k):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!!
        - 1st solution: 588ms, beat 49.1%
        - 2nd solution: 148ms, beat 84.1%
        TP:
        - accumulating result so far and proceed to another DFS round with result so far and rest of the numbers
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def doComb(comb, i):
            if k - len(comb) > (n+1 - i):
                # if number len still needed (k - len(comb)) is bigger than number left (n+1-i),
                # then we don't need to do DFS anymore since we won't have valid combination at the end
                return
            if len(comb) == k:
                res.append(comb)
                return
            for i in range(i, n+1):
                doComb(comb + [i], i + 1) # comb.append(i) won't return anything. but comb + [i] will
        doComb([], 1)
        return res

n = 5
k = 3

print Solution().combine(n, k)