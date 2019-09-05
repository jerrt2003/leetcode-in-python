# -*- coding: utf-8 -*-

class Solution(object):
    def isBipartite(self, graph):
        """
        Sol: DFS
        Perf: Runtime: 160 ms, faster than 52.64% / Memory Usage: 12 MB, less than 40.00%
        T: O(n)
        S: O(n)
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = dict()

        def dfs(pos):
            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]:
                        return False
                else:
                    color[i] = 1 - color[pos]
                    if not dfs(i):
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
            if not dfs(i):
                return False
        return True