# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        Perf: Runtime: 188 ms, faster than 41.82% / Memory Usage: 15.7 MB, less than 12.12%
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        group = hash2.defaultdict(list)
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                group[i+j].append(matrix[i][j])
        res = []
        for k in sorted(group.keys()):
            if k % 2 == 1:
                for v in group[k]:
                    res.append(v)
            else:
                for v in group[k][::-1]:
                    res.append(v)
        return res