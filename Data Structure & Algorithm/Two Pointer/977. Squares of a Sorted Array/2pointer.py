# -*- coding: utf-8 -*-
class Solution(object):
    def sortedSquares(self, A):
        """
        Time: O(n)
        Space: O(n)
        Perf: speed 464ms > 5% / mem: 13.8MB > 37.61%
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return []
        res = list()
        l, r = 0, len(A) - 1
        while l <= r:
            if abs(A[l]) > abs(A[r]):
                res.insert(0, A[l] * A[l])
                l += 1
            else:
                res.insert(0, A[r] * A[r])
                r -= 1
        return res
