class Solution(object):
    def isBipartite(self, graph):
        """
        Facebook
        DFS
        T:O(n) S:O(n)
        Runtime: 216 ms, faster than 27.34% of Python online submissions for Is Graph Bipartite?.
        Memory Usage: 13 MB, less than 77.20% of Python online submissions for Is Graph Bipartite?.
        :type graph: List[List[int]]
        :rtype: bool
        """
        N = len(graph)
        self.graph = graph
        self.group = [0] * N
        for i in range(N):
            if self.group[i] == 0:
                if not self.dfs(i, 1):
                    return False
        return True

    def dfs(self, k, group):
        if self.group[k] == group:
            return True
        elif self.group[k] == -1 * group:
            return False
        self.group[k] = group
        for nei in self.graph[k]:
            if not self.dfs(nei, -1 * group):
                return False
        return True
