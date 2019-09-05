# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        Solution: Graph + BFS
        Time Complexity: O(q(m+n)) --> q: # of queries, m: # of equations, n: # of values
        Space Complexity: O(2m)
        Inspired By: https://leetcode.com/problems/evaluate-division/discuss/88275/Python-fast-BFS-solution-with-detailed-explantion
        TP:
        - a/b = 2.0, b/c = 3.0
          We can build a directed graph:
          a -- 2.0 --> b -- 3.0 --> c
          If we were asked to find a/c, we have:
          a/c = a/b * b/c = 2.0 * 3.0
          In the graph, it is the product of costs of edges.
          Do notice that, 2 edges need to added into the graph with one given equation,
          because with a/b we also get result of b/a, which is the reciprocal of a/b.
          so the previous example also gives edges:
          c -- 0.333 --> b -- 0.5 --> a
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = hash2.defaultdict(list)

        def buildGraph(equations, values):
            for divs, value in zip(equations, values):
                div_a, div_b = divs
                graph[div_a].append([div_b, value])
                graph[div_b].append([div_a, 1/value])

        def get_path(query):
            query_a, query_b = query
            if query_a not in graph or query_b not in graph:
                return -1.0
            stack = graph[query_a][:]
            visited = set()
            while stack:
                target, value = stack.pop(0)
                if target == query_b:
                    return value
                else:
                    for k, v in graph[target]:
                        if k not in visited:
                            stack.append([k, v*value])
                            visited.add(k)
            return -1.0

        buildGraph(equations, values)
        return [get_path(query) for query in queries]

a = [["a","b"],["c","d"]]
b = [1.0,1.0]
c = [["a","c"],["b","d"],["b","a"],["d","c"]]

print Solution().calcEquation(a,b,c)