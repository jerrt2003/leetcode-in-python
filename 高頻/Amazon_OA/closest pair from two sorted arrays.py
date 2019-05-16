# -*- coding: utf-8 -*-
class Solution(object):
    def closestSumOfTwoArray(self, ar1, ar2, x):
        ar1.sort()
        ar2.sort()
        m, n = len(ar1), len(ar2)
        diff = float('inf')
        l, r = 0, n-1
        while l < m and r >= 0:
            if abs(ar1[l]+ar2[r]-x) < diff:
                res1 = ar1[l]
                res2 = ar2[r]
                diff = abs(ar1[l]+ar2[r]-x)
            if ar1[l]+ar2[r] > x:
                r -= 1
            else:
                l += 1
        return res1, res2

print Solution().closestSumOfTwoArray([10, 20, 30, 40],[1, 4, 5, 7],38)

