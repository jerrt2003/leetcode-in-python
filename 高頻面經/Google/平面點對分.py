# -*- coding: utf-8 -*-
import heapq
class Solution(object):
    def usingSlope(self, pts):
        pts.sort(key=lambda x: (x[0], x[1]))
        base_x, base_y = pts.pop(0)

        def compare(pt):
            x_diff = pt[0] - float(base_x)
            y_diff = pt[1] - float(base_y)
            if x_diff == 0:
                slope = float('inf')
            else:
                slope = y_diff/x_diff
            return slope

        pts.sort(key=compare)
        return pts[len(pts)/2]

#pts = [(1,1),(2,1),(1,3),(0,0),(1,0),(1,2)]
pts = [(1,1),(2,2),(1,3),(2,1),(3,1),(4,2),(4,3),(7,3)]
print Solution().usingSlope(pts)