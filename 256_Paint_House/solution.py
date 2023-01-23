from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        self.min_cost = float('inf')
        self.dfs(0, costs, -1, 0)
        return self.min_cost

    def dfs(self, house: int, costs: List[List[int]], prev_color: int, path_cost: int) -> int:
        if house >= len(costs):
            self.min_cost = min(self.min_cost, path_cost)
            return
        for i in range(len(costs[0])):
            if i == prev_color:
                continue
            self.dfs(house+1, costs, i, path_cost+costs[house][i])
        