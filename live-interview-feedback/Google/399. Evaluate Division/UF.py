# -*- coding: utf-8 -*-
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        UF = UnionFind(equations)
        for comps, value in zip(equations, values):
            p1, p2 = comps
            UF.union(p1, p2, value)

        res = []
        for q1, q2 in queries:
            r1 = UF.find(q1)
            r2 = UF.find(q2)
            if not r1[0] or not r2[0] or r1[0] != r2[0]:
                # if q1 not in parent or q2 not in parent --> means they don't exist
                # r1[0] != r2[0] --> means they don't share same parent (root), thus no way to find connection (dis-joint set)
                res.append(-1.0)
            else:
                ans = r1[1]/r2[1]
                # ex.
                # a/c == 3.0 (a's cost to root c is 3.0)
                # b/c == 2.0 (b's cost to root c is 2.0)
                # a/b == ?
                # a/b = a/c * (c/b) --> ans = r1[1]/r2[1]
                res.append(ans)
        return res


class UnionFind(object):
    def __init__(self, eq):
        """
        UF class object constructor
        :param eq:
        """
        self.parent = {}
        for p1, p2 in eq:
            self.parent[p1] = (p1, 1.0)
            self.parent[p2] = (p2, 1.0)

    def find(self, val):
        """
        To find the given 'val' root and val->root path cost
        :param val:
        :return:
        """
        if val not in self.parent:
            return None, None
        if val == self.parent[val][0]: # means we found the root
            return self.parent[val]
        tmp = self.find(self.parent[val][0])
        self.parent[val] = (tmp[0], self.parent[val][1] * tmp[1])
        return self.parent[val]

    def union(self, p1, p2, val):
        """
        To union p1, p2 and update p1->p2 path cost
        :param p1:
        :param p2:
        :param val:
        :return:
        """
        r1 = self.find(p1)
        r2 = self.find(p2)
        if r1[0] != r2[0]:
            self.parent[r1[0]] = (r2[0], r2[1] * val / r1[1])
            # WHY ??
            # self.parent:
            # a d a c
            # c f d f
            # 4 5 3 ?
            # --> c/f = d/f * a/d * c/a = r2[1] * val * 1/r1[1]

a = [ ["a", "b"], ["a", "c"] ]
b = [2.0, 3.0]
c = [ ["b", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

print Solution().calcEquation(a,b,c)
