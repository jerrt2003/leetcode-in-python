# DFS
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.graph = graph

        self.node_color = [0 for _ in range(len(graph))]
        for i in range(len(graph)):
            if self.node_color[i] != 0:
                continue
            if not self.dfs(i, 1):
                return False

        return True

    def dfs(self, node, color):
        if self.node_color[node] != 0 and self.node_color[node] != color:
            return False
        if self.node_color[node] == color:
            return True
        self.node_color[node] = color
        for neighbor in self.graph[node]:
            if (color == 1 and not self.dfs(neighbor, 2)) or (
                color == 2 and not self.dfs(neighbor, 1)
            ):
                return False

        return True
