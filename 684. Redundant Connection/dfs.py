import collections


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        DFS
        T:O(n^2) S:O(n)
        Runtime: 68 ms, faster than 21.98% of Python online submissions for Redundant Connection.
        Memory Usage: 13.8 MB, less than 8.52% of Python online submissions for Redundant Connection.
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)

        def dfs(src, dst):
            if src == dst:
                return True
            if src not in seen:
                seen.add(src)
                return any(dfs(nei, dst) for nei in graph[src])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].append(v)
            graph[v].append(u)