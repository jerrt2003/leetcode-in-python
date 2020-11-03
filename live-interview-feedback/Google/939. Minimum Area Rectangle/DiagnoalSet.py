# -*- coding: utf-8 -*-
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        pts = set()
        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in pts:
                if (x1, y2) in pts and (x2, y1) in pts and x1 != x2 and y1 != y2:
                    res = min(res, abs(x1-x2)*abs(y1-y2))
            pts.add((x1, y1))
        return 0 if res == float('inf') else res


assert Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]) == 4