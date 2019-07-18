# -*- coding: utf-8 -*-
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(stones)
        for i, j in stones:
            uf.union(i, j)

        disjoint_set = set()
        for r in uf.UF.values():
            if r not in disjoint_set:
                disjoint_set.add(r)

        return len(stones) - len(disjoint_set)

class UnionFind(object):
    def __init__(self, stones):
        self.UF = dict()
        self.weight = dict()
        for i, j in stones:
            self.UF[i] = i
            self.UF[10000+j] = 10000+j
            self.weight[i] = 1
            self.weight[10000+j] = 1

    def find(self, i):
        if self.UF[i] != i:
            self.UF[i] = self.find(self.UF[i])
        return self.UF[i]

    def union(self, i, j):
        r1 = self.find(i)
        r2 = self.find(j)
        if r1 != r2:
            if self.weight[r1] > self.weight[r2]:
                self.UF[r2] = r1
            elif self.weight[r2] > self.weight[r1]:
                self.UF[r1] = r2
            else:
                self.UF[r2] = r1
                self.weight[r1] += 1