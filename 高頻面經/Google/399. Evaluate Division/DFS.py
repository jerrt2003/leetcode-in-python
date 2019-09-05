# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        Solution: DFS
        Time Complexity: O(m+n)
        Space Complexity: O(m+n)
        Inspired By: MySELF!! (28ms, beat 23.59%)
        TP:
        - Build the graph just like BFS solution
        - Find path (ex. a-->b-->c) using DFS method
        :param equations:
        :param values:
        :param queries:
        :return:
        """
        graph = hash2.defaultdict(list)

        def buildGraph(equations, values):
            for coords, value in zip(equations, values):
                x, y = coords
                graph[x].append([y, value])
                graph[y].append([x, 1/value])

        def DFS(start, end, res, weight, visited):
            if start not in graph or end not in graph:
                return False
            if start == end:
                res.append(weight)
                return True
            else:
                for k, v in graph[start]:
                    if k not in visited:
                        if DFS(k, end, res, weight * v, visited + [k]):
                            return True
            return False


        buildGraph(equations, values)
        res = []
        for a, b in queries:
            if not DFS(a, b, res, 1.0, []):
                res.append(-1.0)

        return res

a = [ ["a", "b"], ["b", "c"] ]
b = [2.0, 3.0]
c = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

print Solution().calcEquation(a,b,c)