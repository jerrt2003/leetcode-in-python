# -*- coding: utf-8 -*-
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        Time: O(m+n)
        Space: O(m+n)
        Perf: Runtime: 124 ms, faster than 61.24% / Memory Usage: 12.4 MB, less than 78.66%
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        pt_a, pt_b = 0, 0
        res = []
        while pt_a < len(A) and pt_b < len(B):
            lo = max(A[pt_a][0],B[pt_b][0])
            hi = min(A[pt_a][1],B[pt_b][1])

            if lo <= hi:
                res.append([lo, hi])
            if A[pt_a][1] < B[pt_b][1]:
                pt_a += 1
            else:
                pt_b += 1
        return res


assert Solution().intervalIntersection([[0,2],[5,10],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]]) == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
assert Solution().intervalIntersection([[3,10]],[[5,10]]) == [[5,10]]
assert Solution().intervalIntersection([[5,10]],[[5,10]]) == [[5,10]]