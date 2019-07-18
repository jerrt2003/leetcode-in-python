# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m = len(points)
        pts = set(map(tuple, points))
        res = float('inf')
        for i in range(m-1):
            for j in range(1, m):
                a, b = points[i]
                A, B = points[j]
                if (a, B) in pts and (A, b) in pts and (A-a) != 0 and (B-b) != 0:
                    res = min(res, abs(A-a)*abs(B-b))
        return 0 if res == float('inf') else res


assert Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]) == 4