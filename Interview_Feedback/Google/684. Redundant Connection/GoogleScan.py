# -*- coding: utf-8 -*-
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        Time:
        Space:
        Perf: Runtime: 40 ms, faster than 90.31% / Memory Usage: 12 MB, less than 88.82%
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        m = len(edges)
        uf = UnionFind(m)
        res = []
        for u, v in edges:
            if not uf.union(u, v):
                res.append((u, v))
        return res[-1]


class UnionFind(object):
    def __init__(self, m):
        self.parent = [i for i in range(m + 1)]

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, p1, p2):
        r1 = self.find(p1)
        r2 = self.find(p2)

        if r1 != r2:
            self.parent[r2] = r1
            return True
        else:
            return False
