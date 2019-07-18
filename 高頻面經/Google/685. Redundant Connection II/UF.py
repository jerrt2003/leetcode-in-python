# -*- coding: utf-8 -*-
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        cand1, cand2, point_to = None, None, {}
        for p, q in edges:
            if q in point_to:
                cand1, cand2 = point_to[q], (p, q)
                break
            point_to[q] = (p, q)

        uf = UnionFind(len(edges))
        for p, q in edges:
            if (p, q) == cand2:
                continue
            if uf.union(p, q):
                if cand1:
                    return cand1
                return (p, q)
        return cand2

class UnionFind(object):
    def __init__(self, N):
        self.parent = [i for i in range(N+1)]

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        r1 = self.find(i)
        r2 = self.find(j)
        if r1 != r2:
            self.parent[r2] = r1
            return False
        else:
            return True