import collections
import heapq
from typing import List


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        self.ans = -float("inf")
        self.node_neighbors = collections.defaultdict(list)
        for s, e in edges:
            self.node_neighbors[s].append(e)
            self.node_neighbors[e].append(s)

        self.visited = set([0])
        self.dfs(0)

        return self.ans

    def dfs(self, idx) -> int:
        nodes_diameters = []
        for neighbor in self.node_neighbors[idx]:
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                depth = self.dfs(neighbor)

                heapq.heappush(nodes_diameters, depth)
                if len(nodes_diameters) > 2:
                    heapq.heappop(nodes_diameters)

        # leaf node
        if len(nodes_diameters) == 0:
            return 0
        # only one node, just return
        elif len(nodes_diameters) == 1:
            dist = heapq.heappop(nodes_diameters)
            self.ans = max(self.ans, 1 + dist)
            return 1 + dist
        else:
            # multiple children, check diameters first then return
            short = heapq.heappop(nodes_diameters)
            long = heapq.heappop(nodes_diameters)
            self.ans = max(self.ans, 2 + short + long)
            return 1 + long
