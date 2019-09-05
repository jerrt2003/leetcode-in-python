# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def minAreaRect(self, points):
        """
        Solution: Hashtable
        Time Complexity: O(n^3)
        Space Complexity: O(n)
        Perf: Runtime: 2096 ms, faster than 24.86% / Memory Usage: 12.4 MB, less than 22.94%
        Inspired By: https://leetcode.com/problems/minimum-area-rectangle/discuss/244862/Simple-python-solution-with-2-dict
        :type points: List[List[int]]
        :rtype: int
        """
        x_set = hash2.defaultdict(set)
        y_set = hash2.defaultdict(set)
        for x, y in points:
            y_set[x].add(y)
            x_set[y].add(x)
        m = len(points)
        res = float('inf')
        for i in range(m - 1):
            for j in range(i + 1, m):
                p, q = points[i], points[j]
                if p[0] == q[0]:
                    for x in x_set[p[1]]:
                        if x != p[0] and q[1] in y_set[x]:
                            res = min(res, abs(p[1] - q[1]) * abs(x - p[0]))
        return 0 if res == float('inf') else res
