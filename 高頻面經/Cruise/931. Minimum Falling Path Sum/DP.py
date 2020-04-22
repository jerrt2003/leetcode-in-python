# -*- coding: utf-8 -*-
class Solution(object):
    def minFallingPathSum(self, A):
        """
        Sol: DP
        T: O(mn)
        S: O(n)
        Perf: Runtime: 88 ms, faster than 96.24% / Memory Usage: 12.4 MB, less than 57.14%
        :type A: List[List[int]]
        :rtype: int
        """
        if not A or not A[0]:
            return
        res = A[0]
        for i in range(1, len(A)):
            tmp = list()
            for k, v in enumerate(A[i]):
                if k == 0:
                    tmp.append(v + min(res[k], res[k+1]))
                elif k == len(A[i])-1:
                    tmp.append(v + min(res[k], res[k-1]))
                else:
                    tmp.append(v + min(res[k-1],res[k],res[k+1]))
            res = tmp
        return min(res)

A = [[1,2,3],[4,5,6],[7,8,9]]
assert Solution().minFallingPathSum(A) == 12