from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.ans = []

        self.dfs(0, [])

        return self.ans

    def dfs(self, idx, path) -> None:
        if idx == len(self.graph) - 1:
            self.ans.append(path + [idx])
            return

        visited = set(path)
        for neighbor in self.graph[idx]:
            if idx not in visited:
                self.dfs(neighbor, path + [idx])
