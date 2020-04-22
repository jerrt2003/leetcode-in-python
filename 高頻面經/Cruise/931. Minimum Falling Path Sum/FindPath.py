# -*- coding: utf-8 -*-
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
        def findMin(lst, curr_v, curr_k):
            v, path = float('inf'), None
            for prev_v, prev_path in lst:
                if curr_v + prev_v <= v:
                    v = curr_v + prev_v
                    path = prev_path
            return v, path+[curr_k]


        if not A or not A[0]:
            return
        res = [[v, [idx]] for idx, v in enumerate(A[0])]
        for i in range(1, len(A)):
            tmp = list()
            for k, v in enumerate(A[i]):
                if k == 0:
                    tmp.append(findMin([res[k], res[k+1]], v, k))
                elif k == len(A[i])-1:
                    tmp.append(findMin([res[k-1], res[k]], v, k))
                else:
                    tmp.append(findMin([res[k - 1], res[k], res[k + 1]], v, k))
            res = tmp
        a = min(res, key=lambda b: b[0])
        return a[0]

A = [[1,2,3],[4,5,6],[7,8,9]]
assert Solution().minFallingPathSum(A) == 12