# -*- coding: utf-8 -*-
class Solution(object):
    def minAreaFreeRect(self, points):
        """
        T:O(n^3)
        S:O(1)
        Perf: Runtime: 152 ms, faster than 38.39% / Memory Usage: 11.8 MB, less than 82.81%
        :type points: List[List[int]]
        :rtype: float
        """
        m = len(points)
        pts = set((i, j) for i, j in points)
        res = float('inf')
        for i in range(m-2):
            x1, y1 = points[i]
            for j in range(i+1, m):
                x2, y2 = points[j]
                for k in range(j+1, m):
                    x3, y3 = points[k]
                    if not (x3-x1)*(x2-x1) + (y3-y1)*(y2-y1) and (x3+x2-x1, y3+y2-y1) in pts:
                        res = min(res, ((x2-x1)**2 + (y2-y1)**2)**0.5 * ((x3-x1)**2 + (y3-y1)**2)**0.5)
        return 0 if res == float('inf') else res