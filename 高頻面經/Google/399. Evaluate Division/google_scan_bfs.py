# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        Solution: BFS
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Perf: Runtime: 20 ms, faster than 70.35% / Memory Usage: 12 MB, less than 5.56%
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = hash2.defaultdict(list)
        for eq, value in zip(equations, values):
            eq1, eq2 = eq
            graph[eq1].append([eq2, value])
            graph[eq2].append([eq1, 1 / value])

        def bfs(query):
            start, target = query
            if start not in graph or target not in graph:
                return -1
            stack = graph[start][:]
            path = set()
            while stack:
                end, value = stack.pop(0)
                if end == target:
                    return value
                else:
                    for k, v in graph[end]:
                        if k not in path:
                            path.add(k)
                            stack.append((k, value * v))
            return -1

        res = []
        for query in queries:
            res.append(bfs(query))

        return res
