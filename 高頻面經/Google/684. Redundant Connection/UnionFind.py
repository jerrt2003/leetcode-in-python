# -*- coding: utf-8 -*-
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        Solution: Union Find
        Time Complexity:
        Space Complexity:
        Perf: Runtime: 44 ms, faster than 52.37% / Memory Usage: 12.3 MB, less than 6.17%
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        m = len(edges)
        uf = UnionFind(m)
        res = []
        for i, j in edges:
            if not uf.union(i, j):
                res.append([i, j])
        return res[-1]



class UnionFind(object):
    def __init__(self, N):
        self.parent = [None for _ in range(N+1)]
        for i in range(N+1):
            self.parent[i] = i
        self.weight = [1] * (N+1)

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        r1 = self.find(i)
        r2 = self.find(j)

        if r1 != r2:
            if self.weight[r1] > self.weight[r2]:
                self.parent[r2] = r1
            elif self.weight[r2] > self.weight[r1]:
                self.parent[r1] = r2
            else:
                self.parent[r2] = r1
                self.weight[r1] += 1
            return True
        else:
            return False


edges = [[1,2], [1,3], [2,3]]
print Solution().findRedundantConnection(edges)