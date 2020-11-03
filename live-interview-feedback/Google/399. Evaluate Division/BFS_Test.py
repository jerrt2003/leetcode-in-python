# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        mapping = collections.defaultdict(dict)
        for equation, v in zip(equations, values):
            p, q  = equation
            mapping[p][q] = v
            mapping[q][p] = 1/v

        res = []
        for s, e in queries:
            found = False
            if s not in mapping or e not in mapping:
                res.append(-1.0)
                continue
            if s == e:
                res.append(1.0)
                continue
            visited = set([s])
            stack = [(k, v) for k, v in mapping[s].iteritems()]
            while stack:
                cur, totalCost = stack.pop(0)
                if cur == e:
                    res.append(totalCost)
                    found = True
                    break
                for nextP, costToP in mapping[cur].iteritems():
                    if nextP not in visited:
                        stack.append((nextP, totalCost * costToP))
            if not found:
                res.append(-1.0)

        return res

equations = [["a", "b"],["b", "c"]]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

assert Solution().calcEquation(equations, values, queries) == [6.0, 0.5, -1.0, 1.0, -1.0]